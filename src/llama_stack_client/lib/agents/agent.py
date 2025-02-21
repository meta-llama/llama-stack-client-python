# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from typing import Iterator, List, Optional, Tuple, Union

from llama_stack_client import LlamaStackClient
from llama_stack_client.types import ToolResponseMessage, UserMessage
from llama_stack_client.types.agent_create_params import AgentConfig
from llama_stack_client.types.agents.turn import Turn
from llama_stack_client.types.agents.turn_create_params import Document, Toolgroup
from llama_stack_client.types.agents.turn_create_response import (
    AgentTurnResponseStreamChunk,
)
from llama_stack_client.types.shared.tool_call import ToolCall
from llama_stack_client.types.agents.turn import CompletionMessage
from .client_tool import ClientTool
from .tool_parser import ToolParser

DEFAULT_MAX_ITER = 10


class Agent:
    def __init__(
        self,
        client: LlamaStackClient,
        agent_config: AgentConfig,
        client_tools: Tuple[ClientTool] = (),
        tool_parser: Optional[ToolParser] = None,
    ):
        self.client = client
        self.agent_config = agent_config
        self.agent_id = self._create_agent(agent_config)
        self.client_tools = {t.get_name(): t for t in client_tools}
        self.sessions = []
        self.tool_parser = tool_parser
        self.builtin_tools = {}
        for tg in agent_config["toolgroups"]:
            for tool in self.client.tools.list(toolgroup_id=tg):
                self.builtin_tools[tool.identifier] = tool

    def _create_agent(self, agent_config: AgentConfig) -> int:
        agentic_system_create_response = self.client.agents.create(
            agent_config=agent_config,
        )
        self.agent_id = agentic_system_create_response.agent_id
        return self.agent_id

    def create_session(self, session_name: str) -> int:
        agentic_system_create_session_response = self.client.agents.session.create(
            agent_id=self.agent_id,
            session_name=session_name,
        )
        self.session_id = agentic_system_create_session_response.session_id
        self.sessions.append(self.session_id)
        return self.session_id

    def _get_tool_calls(self, chunk: AgentTurnResponseStreamChunk) -> List[ToolCall]:
        if chunk.event.payload.event_type not in ["turn_complete", "turn_awaiting_input"]:
            return []

        message = chunk.event.payload.turn.output_message
        if message.stop_reason == "out_of_tokens":
            return []

        if self.tool_parser:
            return self.tool_parser.get_tool_calls(message)

        return message.tool_calls

    def _get_turn_id(self, chunk: AgentTurnResponseStreamChunk) -> Optional[str]:
        if chunk.event.payload.event_type not in ["turn_complete", "turn_awaiting_input"]:
            return None

        return chunk.event.payload.turn.turn_id

    def _run_tool(self, tool_calls: List[ToolCall]) -> ToolResponseMessage:
        assert len(tool_calls) == 1, "Only one tool call is supported"
        tool_call = tool_calls[0]

        # custom client tools
        if tool_call.tool_name in self.client_tools:
            tool = self.client_tools[tool_call.tool_name]
            # NOTE: tool.run() expects a list of messages, we only pass in last message here
            # but we could pass in the entire message history
            result_message = tool.run(
                [
                    CompletionMessage(
                        role="assistant",
                        content=tool_call.tool_name,
                        tool_calls=[tool_call],
                        stop_reason="end_of_turn",
                    )
                ]
            )
            return result_message

        # builtin tools executed by tool_runtime
        if tool_call.tool_name in self.builtin_tools:
            tool_result = self.client.tool_runtime.invoke_tool(
                tool_name=tool_call.tool_name,
                kwargs=tool_call.arguments,
            )
            tool_response_message = ToolResponseMessage(
                call_id=tool_call.call_id,
                tool_name=tool_call.tool_name,
                content=tool_result.content,
                role="tool",
            )
            return tool_response_message

        # cannot find tools
        return ToolResponseMessage(
            call_id=tool_call.call_id,
            tool_name=tool_call.tool_name,
            content=f"Unknown tool `{tool_call.tool_name}` was called.",
            role="tool",
        )

    def create_turn(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        stream: bool = True,
    ) -> Iterator[AgentTurnResponseStreamChunk] | Turn:
        if stream:
            return self._create_turn_streaming(messages, session_id, toolgroups, documents)
        else:
            chunks = []
            for chunk in self._create_turn_streaming(messages, session_id, toolgroups, documents):
                if chunk.event.payload.event_type in ["turn_complete", "turn_awaiting_input"]:
                    chunks.append(chunk)
                pass
            if not chunks:
                raise Exception("Turn did not complete")

            # merge chunks
            return Turn(
                input_messages=chunks[0].event.payload.turn.input_messages,
                output_message=chunks[-1].event.payload.turn.output_message,
                session_id=chunks[0].event.payload.turn.session_id,
                steps=[step for chunk in chunks for step in chunk.event.payload.turn.steps],
                turn_id=chunks[0].event.payload.turn.turn_id,
                started_at=chunks[0].event.payload.turn.started_at,
                completed_at=chunks[-1].event.payload.turn.completed_at,
                output_attachments=[
                    attachment for chunk in chunks for attachment in chunk.event.payload.turn.output_attachments
                ],
            )

    def _create_turn_streaming(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
    ) -> Iterator[AgentTurnResponseStreamChunk]:
        stop = False
        n_iter = 0
        max_iter = self.agent_config.get("max_infer_iters", DEFAULT_MAX_ITER)

        # 1. create an agent turn
        turn_response = self.client.agents.turn.create(
            agent_id=self.agent_id,
            # use specified session_id or last session created
            session_id=session_id or self.session_id[-1],
            messages=messages,
            stream=True,
            documents=documents,
            toolgroups=toolgroups,
        )
        is_turn_complete = True
        turn_id = None
        for chunk in turn_response:
            tool_calls = self._get_tool_calls(chunk)
            if hasattr(chunk, "error"):
                yield chunk
                return
            elif not tool_calls:
                yield chunk
            else:
                is_turn_complete = False
                turn_id = self._get_turn_id(chunk)
                yield chunk
                break

        # 2. while the turn is not complete, continue the turn
        while not is_turn_complete and n_iter < max_iter:
            is_turn_complete = True
            assert turn_id is not None, "turn_id is None"

            # run the tools
            tool_response_message = self._run_tool(tool_calls)

            continue_response = self.client.agents.turn.continue_(
                agent_id=self.agent_id,
                session_id=session_id or self.session_id[-1],
                turn_id=turn_id,
                tool_responses=[tool_response_message],
                stream=True,
            )
            for chunk in continue_response:
                tool_calls = self._get_tool_calls(chunk)
                if hasattr(chunk, "error"):
                    yield chunk
                    return
                elif not tool_calls:
                    yield chunk
                else:
                    is_turn_complete = False
                    turn_id = self._get_turn_id(chunk)
                    n_iter += 1

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
from llama_stack_client.types.agents.turn_create_response import AgentTurnResponseStreamChunk
from llama_stack_client.types.shared.tool_call import ToolCall

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
        if chunk.event.payload.event_type != "turn_complete":
            return None

        message = chunk.event.payload.turn.output_message
        if message.stop_reason == "out_of_tokens":
            return None

        if self.tool_parser:
            return self.tool_parser.get_tool_calls(message)

        return message.tool_calls

    def _run_tool(self, chunk: AgentTurnResponseStreamChunk, tool_calls: List[ToolCall]) -> ToolResponseMessage:
        message = chunk.event.payload.turn.output_message
        message.tool_calls = tool_calls
        tool_call = message.tool_calls[0]

        # custom client tools
        if tool_call.tool_name in self.client_tools:
            tool = self.client_tools[tool_call.tool_name]
            # NOTE: tool.run() expects a list of messages, we only pass in last message here
            # but we could pass in the entire message history
            result_message = tool.run([message])
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
            return self._create_turn_streaming(messages, session_id, toolgroups, documents, stream)
        else:
            chunk = None
            for chunk in self._create_turn_streaming(messages, session_id, toolgroups, documents, stream):
                pass
            if not chunk:
                raise Exception("No chunk returned")
            if chunk.event.payload.event_type != "turn_complete":
                raise Exception("Turn did not complete")
            return chunk.event.payload.turn

    def _create_turn_streaming(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        stream: bool = True,
    ) -> Iterator[AgentTurnResponseStreamChunk]:
        stop = False
        n_iter = 0
        max_iter = self.agent_config.get("max_infer_iters", DEFAULT_MAX_ITER)
        while not stop and n_iter < max_iter:
            response = self.client.agents.turn.create(
                agent_id=self.agent_id,
                # use specified session_id or last session created
                session_id=session_id or self.session_id[-1],
                messages=messages,
                stream=True,
                documents=documents,
                toolgroups=toolgroups,
            )
            # by default, we stop after the first turn
            stop = True
            for chunk in response:
                tool_calls = self._get_tool_calls(chunk)
                if hasattr(chunk, "error"):
                    yield chunk
                    return
                elif not tool_calls:
                    yield chunk
                else:
                    next_message = self._run_tool(chunk, tool_calls)
                    yield next_message

                    # continue the turn when there's a tool call
                    stop = False
                    messages = [next_message]
                    n_iter += 1

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
from llama_stack_client.types.agents.turn_response_event import TurnResponseEvent
from llama_stack_client.types.agents.turn_response_event_payload import (
    AgentTurnResponseStepCompletePayload,
)
from llama_stack_client.types.shared.tool_call import ToolCall
from llama_stack_client.types.agents.turn import CompletionMessage
from .client_tool import ClientTool
from .tool_parser import ToolParser
from datetime import datetime
import uuid
from llama_stack_client.types.tool_execution_step import ToolExecutionStep
from llama_stack_client.types.tool_response import ToolResponse

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
            return []

        message = chunk.event.payload.turn.output_message
        if message.stop_reason == "out_of_tokens":
            return []

        if self.tool_parser:
            return self.tool_parser.get_tool_calls(message)

        return message.tool_calls

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
                if chunk.event.payload.event_type == "turn_complete":
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
                    tool_execution_start_time = datetime.now()
                    tool_response_message = self._run_tool(tool_calls)
                    tool_execution_step = ToolExecutionStep(
                        step_type="tool_execution",
                        step_id=str(uuid.uuid4()),
                        tool_calls=tool_calls,
                        tool_responses=[
                            ToolResponse(
                                tool_name=tool_response_message.tool_name,
                                content=tool_response_message.content,
                                call_id=tool_response_message.call_id,
                            )
                        ],
                        turn_id=chunk.event.payload.turn.turn_id,
                        completed_at=datetime.now(),
                        started_at=tool_execution_start_time,
                    )
                    yield AgentTurnResponseStreamChunk(
                        event=TurnResponseEvent(
                            payload=AgentTurnResponseStepCompletePayload(
                                event_type="step_complete",
                                step_id=tool_execution_step.step_id,
                                step_type="tool_execution",
                                step_details=tool_execution_step,
                            )
                        )
                    )

                    # HACK: append the tool execution step to the turn
                    chunk.event.payload.turn.steps.append(tool_execution_step)
                    yield chunk

                    # continue the turn when there's a tool call
                    stop = False
                    messages = [tool_response_message]
                    n_iter += 1

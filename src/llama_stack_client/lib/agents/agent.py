# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import logging
from typing import Iterator, List, Optional, Tuple, Union

from llama_stack_client import LlamaStackClient

from llama_stack_client.types import ToolResponseMessage, ToolResponseParam, UserMessage
from llama_stack_client.types.agent_create_params import AgentConfig
from llama_stack_client.types.agents.turn import CompletionMessage, Turn
from llama_stack_client.types.agents.turn_create_params import Document, Toolgroup
from llama_stack_client.types.agents.turn_create_response import AgentTurnResponseStreamChunk
from llama_stack_client.types.shared.tool_call import ToolCall
from llama_stack_client.types.shared_params.agent_config import ToolConfig
from llama_stack_client.types.shared_params.response_format import ResponseFormat
from llama_stack_client.types.shared_params.sampling_params import SamplingParams

from .client_tool import ClientTool
from .tool_parser import ToolParser

DEFAULT_MAX_ITER = 10

logger = logging.getLogger(__name__)


class Agent:
    def __init__(
        self,
        client: LlamaStackClient,
        # begin deprecated
        agent_config: Optional[AgentConfig] = None,
        client_tools: Tuple[ClientTool, ...] = (),
        # end deprecated
        tool_parser: Optional[ToolParser] = None,
        model: Optional[str] = None,
        instructions: Optional[str] = None,
        tools: Optional[List[Union[Toolgroup, ClientTool]]] = None,
        tool_config: Optional[ToolConfig] = None,
        sampling_params: Optional[SamplingParams] = None,
        max_infer_iters: Optional[int] = None,
        input_shields: Optional[List[str]] = None,
        output_shields: Optional[List[str]] = None,
        response_format: Optional[ResponseFormat] = None,
        enable_session_persistence: Optional[bool] = None,
    ):
        """Construct an Agent with the given parameters.

        :param client: The LlamaStackClient instance.
        :param agent_config: The AgentConfig instance.
            ::deprecated: use other parameters instead
        :param client_tools: A tuple of ClientTool instances.
            ::deprecated: use tools instead
        :param tool_parser: Custom logic that parses tool calls from a message.
        :param model: The model to use for the agent.
        :param instructions: The instructions for the agent.
        :param tools: A list of tools for the agent. Values can be one of the following:
            - dict representing a toolgroup/tool with arguments: e.g. {"name": "builtin::rag/knowledge_search", "args": {"vector_db_ids": [123]}}
            - a python function decorated with @client_tool
            - str representing a tool within a toolgroup: e.g. "builtin::rag/knowledge_search"
            - str representing a toolgroup_id: e.g. "builtin::rag", "builtin::code_interpreter", where all tools in the toolgroup will be added to the agent
            - an instance of ClientTool: A client tool object.
        :param tool_config: The tool configuration for the agent.
        :param sampling_params: The sampling parameters for the agent.
        :param max_infer_iters: The maximum number of inference iterations.
        :param input_shields: The input shields for the agent.
        :param output_shields: The output shields for the agent.
        :param response_format: The response format for the agent.
        :param enable_session_persistence: Whether to enable session persistence.
        """
        self.client = client

        if agent_config is not None:
            logger.warning("`agent_config` is deprecated. Use inlined parameters instead.")
        if client_tools != ():
            logger.warning("`client_tools` is deprecated. Use `tools` instead.")

        # Construct agent_config from parameters if not provided
        if agent_config is None:
            # Create a minimal valid AgentConfig with required fields
            if model is None or instructions is None:
                raise ValueError("Both 'model' and 'instructions' are required when agent_config is not provided")

            agent_config = {
                "model": model,
                "instructions": instructions,
            }

            # Add optional parameters if provided
            if enable_session_persistence is not None:
                agent_config["enable_session_persistence"] = enable_session_persistence
            if max_infer_iters is not None:
                agent_config["max_infer_iters"] = max_infer_iters
            if input_shields is not None:
                agent_config["input_shields"] = input_shields
            if output_shields is not None:
                agent_config["output_shields"] = output_shields
            if response_format is not None:
                agent_config["response_format"] = response_format
            if sampling_params is not None:
                agent_config["sampling_params"] = sampling_params
            if tool_config is not None:
                agent_config["tool_config"] = tool_config
            if tools is not None:
                toolgroups: List[Toolgroup] = []
                client_tools: List[ClientTool] = []

                for tool in tools:
                    if isinstance(tool, str) or isinstance(tool, dict):
                        toolgroups.append(tool)
                    else:
                        client_tools.append(tool)

                agent_config["toolgroups"] = toolgroups
                agent_config["client_tools"] = [tool.get_tool_definition() for tool in client_tools]

            agent_config = AgentConfig(**agent_config)

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

    def create_session(self, session_name: str) -> str:
        agentic_system_create_session_response = self.client.agents.session.create(
            agent_id=self.agent_id,
            session_name=session_name,
        )
        self.session_id = agentic_system_create_session_response.session_id
        self.sessions.append(self.session_id)
        return self.session_id

    def _get_tool_calls(self, chunk: AgentTurnResponseStreamChunk) -> List[ToolCall]:
        if chunk.event.payload.event_type not in {"turn_complete", "turn_awaiting_input"}:
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

    def _run_tool(self, tool_calls: List[ToolCall]) -> ToolResponseParam:
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
            tool_response = ToolResponseParam(
                call_id=tool_call.call_id,
                tool_name=tool_call.tool_name,
                content=tool_result.content,
            )
            return tool_response

        # cannot find tools
        return ToolResponseParam(
            call_id=tool_call.call_id,
            tool_name=tool_call.tool_name,
            content=f"Unknown tool `{tool_call.tool_name}` was called.",
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
            chunks = [x for x in self._create_turn_streaming(messages, session_id, toolgroups, documents)]
            if not chunks:
                raise Exception("Turn did not complete")
            return chunks[-1].event.payload.turn

    def _create_turn_streaming(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
    ) -> Iterator[AgentTurnResponseStreamChunk]:
        n_iter = 0

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

        # 2. process turn and resume if there's a tool call
        is_turn_complete = False
        while not is_turn_complete:
            is_turn_complete = True
            for chunk in turn_response:
                if hasattr(chunk, "error"):
                    yield chunk
                    return
                tool_calls = self._get_tool_calls(chunk)
                if not tool_calls:
                    yield chunk
                else:
                    is_turn_complete = False
                    # End of turn is reached, do not resume even if there's a tool call
                    # We only check for this if tool_parser is not set, because otherwise
                    # tool call will be parsed on client side, and server will always return "end_of_turn"
                    if not self.tool_parser and chunk.event.payload.turn.output_message.stop_reason in {"end_of_turn"}:
                        yield chunk
                        break

                    turn_id = self._get_turn_id(chunk)
                    if n_iter == 0:
                        yield chunk

                    # run the tools
                    tool_response = self._run_tool(tool_calls)

                    # pass it to next iteration
                    turn_response = self.client.agents.turn.resume(
                        agent_id=self.agent_id,
                        session_id=session_id or self.session_id[-1],
                        turn_id=turn_id,
                        tool_responses=[tool_response],
                        stream=True,
                    )
                    n_iter += 1

            if n_iter > self.agent_config.get("max_infer_iters", DEFAULT_MAX_ITER):
                raise Exception("Max inference iterations reached")

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

import re
import json
from typing import Dict, Any

from llama_stack_client.types.shared.tool_call import ToolCall

from .client_tool import ClientTool

DEFAULT_MAX_ITER = 10


def maybe_extract_action(text: str) -> Optional[Tuple[str, Dict[str, Any]]]:
    """
    Extract action name and parameters from the text format:

    Thought: <some_text>

    Action:
    {
      "action": <action_name>,
      "action_input": <action_params>
    }<end_action>

    Args:
        text (str): Input text containing the action block

    Returns:
        Tuple[str, Dict[str, Any]]: Tuple of (action_name, action_parameters)

    Raises:
        ValueError: If the action block cannot be parsed or is missing required fields
    """
    try:
        # Find the action block using regex
        action_pattern = r'Action:\s*{\s*"action":\s*"([^"]+)",\s*"action_input":\s*({[^}]+})\s*}<end_action>'
        match = re.search(action_pattern, text, re.DOTALL)

        if not match:
            raise ValueError("Could not find valid action block in text")

        action_name = match.group(1)
        action_params = json.loads(match.group(2))

        return action_name, action_params
    except (ValueError, json.JSONDecodeError) as e:
        print(f"Error parsing action: {e}")
        return None


class Agent:
    def __init__(
        self,
        client: LlamaStackClient,
        agent_config: AgentConfig,
        client_tools: Tuple[ClientTool] = (),
        memory_bank_id: Optional[str] = None,
    ):
        self.client = client
        self.agent_config = agent_config
        self.agent_id = self._create_agent(agent_config)
        self.client_tools = {t.get_name(): t for t in client_tools}
        self.sessions = []
        self.memory_bank_id = memory_bank_id

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

    def _has_tool_call(self, chunk: AgentTurnResponseStreamChunk) -> bool:
        if chunk.event.payload.event_type != "turn_complete":
            return False
        message = chunk.event.payload.turn.output_message
        if message.stop_reason == "out_of_tokens":
            return False

        # Has tool call if it is using the ReAct pattern
        action = maybe_extract_action(message.content)
        if action and action[0] in self.client_tools:
            message.tool_calls = [
                ToolCall(
                    call_id="random-id",
                    tool_name=action[0],
                    arguments=action[1],
                )
            ]
            print(f"!!Action: {action}")

        return len(message.tool_calls) > 0

    def _run_tool(self, chunk: AgentTurnResponseStreamChunk) -> ToolResponseMessage:
        message = chunk.event.payload.turn.output_message
        tool_call = message.tool_calls[0]
        if tool_call.tool_name not in self.client_tools:
            return ToolResponseMessage(
                call_id=tool_call.call_id,
                tool_name=tool_call.tool_name,
                content=f"Unknown tool `{tool_call.tool_name}` was called.",
                role="ipython",
            )
        tool = self.client_tools[tool_call.tool_name]
        result_messages = tool.run([message])
        next_message = result_messages[0]
        return next_message

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
                if hasattr(chunk, "error"):
                    yield chunk
                    return
                elif not self._has_tool_call(chunk):
                    yield chunk
                else:
                    from rich.pretty import pprint

                    print("Running Tools...")
                    pprint(chunk)
                    next_message = self._run_tool(chunk)
                    yield next_message

                    # continue the turn when there's a tool call
                    stop = False
                    messages = [next_message]
                    n_iter += 1

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from typing import List, Optional, Tuple, Union

from llama_stack_client import LlamaStackClient
from llama_stack_client.types import Attachment, ToolResponseMessage, UserMessage
from llama_stack_client.types.agent_create_params import AgentConfig
from .custom_tool import CustomTool


class Agent:
    def __init__(self, client: LlamaStackClient, agent_config: AgentConfig, custom_tools: Tuple[CustomTool] = ()):
        self.client = client
        self.agent_config = agent_config
        self.agent_id = self._create_agent(agent_config)
        self.custom_tools = {t.get_name(): t for t in custom_tools}
        self.sessions = []

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

    async def create_turn(
        self, messages: List[Union[UserMessage, ToolResponseMessage]], attachments: Optional[List[Attachment]] = None, session_id: Optional[str] = None,
    ):
        response = self.client.agents.turn.create(
            agent_id=self.agent_id,
            # use specified session_id or last session created
            session_id=session_id or self.session_id[-1],
            messages=messages,
            attachments=attachments,
            stream=True,
        )
        turn = None
        for chunk in response:
            if chunk.event.payload.event_type != "turn_complete":
                yield chunk
            else:
                turn = chunk.event.payload.turn

        message = turn.output_message
        if len(message.tool_calls) == 0:
            yield chunk
            return

        if message.stop_reason == "out_of_tokens":
            yield chunk
            return

        tool_call = message.tool_calls[0]
        if tool_call.tool_name not in self.custom_tools:
            m = ToolResponseMessage(
                call_id=tool_call.call_id,
                tool_name=tool_call.tool_name,
                content=f"Unknown tool `{tool_call.tool_name}` was called. Try again with something else",
                role="ipython",
            )
            next_message = m
        else:
            tool = self.custom_tools[tool_call.tool_name]
            result_messages = await self.execute_custom_tool(tool, message)
            next_message = result_messages[0]

        yield next_message

    async def execute_custom_tool(
        self, tool: CustomTool, message: Union[UserMessage, ToolResponseMessage]
    ) -> List[Union[UserMessage, ToolResponseMessage]]:
        result_messages = await tool.run([message])
        return result_messages

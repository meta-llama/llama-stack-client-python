# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from pydantic import BaseModel
from typing import Dict, Any
from ..agent import Agent
from .output_parser import ReActOutputParser
from ..output_parser import OutputParser
from .prompts import DEFAULT_REACT_AGENT_SYSTEM_PROMPT_TEMPLATE

from typing import Tuple, Optional
from llama_stack_client import LlamaStackClient
from ..client_tool import ClientTool
from llama_stack_client.types.agent_create_params import AgentConfig


class Action(BaseModel):
    tool_name: str
    tool_params: Dict[str, Any]


class ReActOutput(BaseModel):
    thought: str
    action: Optional[Action] = None
    answer: Optional[str] = None


class ReActAgent(Agent):
    """ReAct agent.

    Simple wrapper around Agent to add prepare prompts for creating a ReAct agent from a list of tools.
    """

    def __init__(
        self,
        client: LlamaStackClient,
        model: str,
        builtin_toolgroups: Tuple[str] = (),
        client_tools: Tuple[ClientTool] = (),
        output_parser: OutputParser = ReActOutputParser(),
        json_response_format: bool = False,
        custom_agent_config: Optional[AgentConfig] = None,
    ):
        def get_tool_definition(tool):
            return {
                "name": tool.identifier,
                "description": tool.description,
                "parameters": tool.parameters,
            }

        if custom_agent_config is None:
            tool_names = ""
            tool_descriptions = ""
            for x in builtin_toolgroups:
                tool_names += ", ".join([tool.identifier for tool in client.tools.list(toolgroup_id=x)])
                tool_descriptions += "\n".join(
                    [f"- {tool.identifier}: {get_tool_definition(tool)}" for tool in client.tools.list(toolgroup_id=x)]
                )

            tool_names += ", "
            tool_descriptions += "\n"
            tool_names += ", ".join([tool.get_name() for tool in client_tools])
            tool_descriptions += "\n".join(
                [f"- {tool.get_name()}: {tool.get_tool_definition()}" for tool in client_tools]
            )

            instruction = DEFAULT_REACT_AGENT_SYSTEM_PROMPT_TEMPLATE.replace("<<tool_names>>", tool_names).replace(
                "<<tool_descriptions>>", tool_descriptions
            )

            # user default toolgroups
            agent_config = AgentConfig(
                model=model,
                instructions=instruction,
                toolgroups=builtin_toolgroups,
                client_tools=[client_tool.get_tool_definition() for client_tool in client_tools],
                tool_choice="auto",
                # TODO: refactor this to use SystemMessageBehaviour.replace
                tool_prompt_format="json",
                input_shields=[],
                output_shields=[],
                enable_session_persistence=False,
            )

        if json_response_format:
            agent_config.response_format = {
                "type": "json_schema",
                "json_schema": ReActOutput.model_json_schema(),
            }

        super().__init__(
            client=client,
            agent_config=agent_config,
            client_tools=client_tools,
            output_parser=output_parser,
        )

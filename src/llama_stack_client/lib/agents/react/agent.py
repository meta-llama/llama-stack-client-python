# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from typing import Any, Dict, Optional, Tuple

from llama_stack_client import LlamaStackClient
from llama_stack_client.types.agent_create_params import AgentConfig
from pydantic import BaseModel

from ..agent import Agent
from ..client_tool import ClientTool
from ..tool_parser import ToolParser
from .prompts import DEFAULT_REACT_AGENT_SYSTEM_PROMPT_TEMPLATE
from .tool_parser import ReActToolParser


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
        tool_parser: ToolParser = ReActToolParser(),
        json_response_format: bool = False,
        custom_agent_config: Optional[AgentConfig] = None,
    ):
        def get_tool_defs():
            tool_defs = []
            for x in builtin_toolgroups:
                tool_defs.extend(
                    [
                        {
                            "name": tool.identifier,
                            "description": tool.description,
                            "parameters": tool.parameters,
                        }
                        for tool in client.tools.list(toolgroup_id=x)
                    ]
                )
            tool_defs.extend(
                [
                    {
                        "name": tool.get_name(),
                        "description": tool.get_description(),
                        "parameters": tool.get_params_definition(),
                    }
                    for tool in client_tools
                ]
            )
            return tool_defs

        if custom_agent_config is None:
            tool_names, tool_descriptions = "", ""
            tool_defs = get_tool_defs()
            tool_names = ", ".join([x["name"] for x in tool_defs])
            tool_descriptions = "\n".join([f"- {x['name']}: {x}" for x in tool_defs])
            instruction = DEFAULT_REACT_AGENT_SYSTEM_PROMPT_TEMPLATE.replace(
                "<<tool_names>>", tool_names
            ).replace("<<tool_descriptions>>", tool_descriptions)

            # user default toolgroups
            agent_config = AgentConfig(
                model=model,
                instructions=instruction,
                toolgroups=builtin_toolgroups,
                client_tools=[
                    client_tool.get_tool_definition() for client_tool in client_tools
                ],
                tool_config={
                    "tool_choice": "auto",
                    "tool_prompt_format": "json" if "3.1" in model else "python_list",
                    "system_message_behavior": "replace",
                },
                input_shields=[],
                output_shields=[],
                enable_session_persistence=False,
            )
        else:
            agent_config = custom_agent_config

        if json_response_format:
            agent_config.response_format = {
                "type": "json_schema",
                "json_schema": ReActOutput.model_json_schema(),
            }

        super().__init__(
            client=client,
            agent_config=agent_config,
            client_tools=client_tools,
            tool_parser=tool_parser,
        )

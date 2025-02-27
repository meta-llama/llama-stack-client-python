# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from typing import Any, Dict, Optional

from llama_stack_client import LlamaStackClient
from llama_stack_client.types.agent_create_params import AgentConfig
from pydantic import BaseModel

from ..agent import Agent
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
        agent_config: AgentConfig,
        tool_parser: ToolParser = ReActToolParser(),
        json_response_format: bool = False,
    ):
        self.agent_config = agent_config

        def get_tool_defs():
            tool_defs = []
            for x in agent_config["toolgroups"]:
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
                    for tool in agent_config["client_tools"]
                ]
            )
            return tool_defs

        tool_names, tool_descriptions = "", ""
        tool_defs = get_tool_defs()
        tool_names = ", ".join([x["name"] for x in tool_defs])
        tool_descriptions = "\n".join([f"- {x['name']}: {x}" for x in tool_defs])
        instruction = DEFAULT_REACT_AGENT_SYSTEM_PROMPT_TEMPLATE.replace("<<tool_names>>", tool_names).replace(
            "<<tool_descriptions>>", tool_descriptions
        )

        agent_config["instructions"] = instruction

        if json_response_format:
            agent_config.response_format = {
                "type": "json_schema",
                "json_schema": ReActOutput.model_json_schema(),
            }

        super().__init__(
            client=client,
            agent_config=agent_config,
            tool_parser=tool_parser,
        )

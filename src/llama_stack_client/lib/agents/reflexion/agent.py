# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from typing import Any, Dict, Optional, Tuple, List

from llama_stack_client import LlamaStackClient
from llama_stack_client.types.agent_create_params import AgentConfig
from pydantic import BaseModel

from ..agent import Agent
from ..client_tool import ClientTool
from ..tool_parser import ToolParser
from .prompts import DEFAULT_REFLEXION_AGENT_SYSTEM_PROMPT_TEMPLATE

from .tool_parser import ReflexionToolParser


class Action(BaseModel):
    tool_name: str
    tool_params: Dict[str, Any]


class ReflexionOutput(BaseModel):
    thought: str
    reflection: Optional[str] = None
    action: Optional[Action] = None
    answer: Optional[str] = None


class ReflexionAgent(Agent):
    """Reflexion agent.

    Extends ReAct agent with self-reflection capabilities to improve reasoning and tool use.
    """

    def __init__(
        self,
        client: LlamaStackClient,
        model: str,
        builtin_toolgroups: Tuple[str] = (),
        client_tools: Tuple[ClientTool] = (),
        tool_parser: ToolParser = ReflexionToolParser(),
        json_response_format: bool = False,
        custom_agent_config: Optional[AgentConfig] = None,
    ):
        # Dictionary to store reflections for each session
        self.reflection_memory = {}

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
            instruction = DEFAULT_REFLEXION_AGENT_SYSTEM_PROMPT_TEMPLATE.replace("<<tool_names>>", tool_names).replace(
                "<<tool_descriptions>>", tool_descriptions
            )

            # user default toolgroups
            agent_config = AgentConfig(
                model=model,
                instructions=instruction,
                toolgroups=builtin_toolgroups,
                client_tools=[client_tool.get_tool_definition() for client_tool in client_tools],
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
                "json_schema": ReflexionOutput.model_json_schema(),
            }

        super().__init__(
            client=client,
            model=model,
            agent_config=agent_config,
            tool_parser=tool_parser,
            client_tools=client_tools,
        )

    def create_turn(self, messages, session_id, stream=False, **kwargs):
        """Override create_turn to add reflection to the context"""
        
        # If we have reflections for this session, add them to the context
        if session_id in self.reflection_memory and self.reflection_memory[session_id]:
            # Create a system message with past reflections
            reflection_summary = "\n".join(self.reflection_memory[session_id])
            reflection_message = {
                "role": "system", 
                "content": f"Your past reflections:\n{reflection_summary}\n\nUse these reflections to improve your reasoning."
            }
            
            # Insert reflection message before the user message
            for i, msg in enumerate(messages):
                if msg["role"] == "user":
                    messages.insert(i, reflection_message)
                    break
        
        # Call the parent method to process the turn
        response = super().create_turn(messages, session_id, stream, **kwargs)
        
        # Store any new reflections
        if not stream:
            try:
                # Extract reflection from response
                content = response.choices[0].message.content
                reflexion_output = ReflexionOutput.model_validate_json(content)
                
                if reflexion_output.reflection:
                    if session_id not in self.reflection_memory:
                        self.reflection_memory[session_id] = []
                    
                    self.reflection_memory[session_id].append(reflexion_output.reflection)
            except Exception as e:
                print(f"Failed to extract reflection: {e}")
        
        return response
# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..tool_def_param import ToolDefParam
from .response_format import ResponseFormat
from .sampling_params import SamplingParams

__all__ = ["AgentConfig", "ToolConfig", "Toolgroup", "ToolgroupAgentToolGroupWithArgs"]


class ToolConfig(TypedDict, total=False):
    system_message_behavior: Literal["append", "replace"]
    """(Optional) Config for how to override the default system prompt.

    - `SystemMessageBehavior.append`: Appends the provided system message to the
      default system prompt. - `SystemMessageBehavior.replace`: Replaces the default
      system prompt with the provided system message. The system message can include
      the string '{{function_definitions}}' to indicate where the function
      definitions should be inserted.
    """

    tool_choice: Union[Literal["auto", "required", "none"], str]
    """(Optional) Whether tool use is automatic, required, or none.

    Can also specify a tool name to use a specific tool. Defaults to
    ToolChoice.auto.
    """

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """(Optional) Instructs the model how to format tool calls.

    By default, Llama Stack will attempt to use a format that is best adapted to the
    model. - `ToolPromptFormat.json`: The tool calls are formatted as a JSON
    object. - `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
    <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
    are output as Python syntax -- a list of function calls.
    """


class ToolgroupAgentToolGroupWithArgs(TypedDict, total=False):
    args: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    name: Required[str]


Toolgroup: TypeAlias = Union[str, ToolgroupAgentToolGroupWithArgs]


class AgentConfig(TypedDict, total=False):
    instructions: Required[str]

    model: Required[str]

    client_tools: Iterable[ToolDefParam]

    enable_session_persistence: bool

    input_shields: List[str]

    max_infer_iters: int

    output_shields: List[str]

    response_format: ResponseFormat
    """Configuration for JSON schema-guided response generation."""

    sampling_params: SamplingParams

    tool_choice: Literal["auto", "required", "none"]
    """Whether tool use is required or automatic.

    This is a hint to the model which may not be followed. It depends on the
    Instruction Following capabilities of the model.
    """

    tool_config: ToolConfig
    """Configuration for tool use."""

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """Prompt format for calling custom / zero shot tools."""

    toolgroups: List[Toolgroup]

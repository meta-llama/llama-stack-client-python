# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .sampling_params import SamplingParams
from .memory_tool_definition import MemoryToolDefinition
from .search_tool_definition import SearchToolDefinition
from .photogen_tool_definition import PhotogenToolDefinition
from .function_call_tool_definition import FunctionCallToolDefinition
from .wolfram_alpha_tool_definition import WolframAlphaToolDefinition
from .code_interpreter_tool_definition import CodeInterpreterToolDefinition

__all__ = ["AgentConfig", "Tool"]

Tool: TypeAlias = Union[
    SearchToolDefinition,
    WolframAlphaToolDefinition,
    PhotogenToolDefinition,
    CodeInterpreterToolDefinition,
    FunctionCallToolDefinition,
    MemoryToolDefinition,
]


class AgentConfig(TypedDict, total=False):
    enable_session_persistence: Required[bool]

    instructions: Required[str]

    max_infer_iters: Required[int]

    model: Required[str]

    input_shields: List[str]

    output_shields: List[str]

    sampling_params: SamplingParams

    tool_choice: Literal["auto", "required"]

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """
    `json` -- Refers to the json format for calling tools. The json format takes the
    form like { "type": "function", "function" : { "name": "function_name",
    "description": "function_description", "parameters": {...} } }

    `function_tag` -- This is an example of how you could define your own user
    defined format for making tool calls. The function_tag format looks like this,
    <function=function_name>(parameters)</function>

    The detailed prompts for each of these formats are added to llama cli
    """

    tools: Iterable[Tool]

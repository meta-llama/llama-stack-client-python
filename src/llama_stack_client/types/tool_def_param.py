# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolDefParam", "Parameter"]


class Parameter(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameter_type: Required[str]

    required: Required[bool]

    default: Union[bool, float, str, Iterable[object], object, None]


class ToolDefParam(TypedDict, total=False):
    name: Required[str]

    description: str

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    parameters: Iterable[Parameter]

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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..tool_def_param import ToolDefParam
from .response_format import ResponseFormat
from .sampling_params import SamplingParams

__all__ = ["AgentConfig", "Toolgroup", "ToolgroupUnionMember1"]


class ToolgroupUnionMember1(TypedDict, total=False):
    args: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    name: Required[str]


Toolgroup: TypeAlias = Union[str, ToolgroupUnionMember1]

class ToolConfig(TypedDict, total=False):
    tool_choice: Literal["auto", "required"]
    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    system_message_behavior: Literal["append", "replace"]


class AgentConfig(TypedDict, total=False):
    enable_session_persistence: Required[bool]

    instructions: Required[str]

    max_infer_iters: Required[int]

    model: Required[str]

    client_tools: Iterable[ToolDefParam]

    input_shields: List[str]

    output_shields: List[str]

    response_format: ResponseFormat

    sampling_params: SamplingParams

    # DEPRECATED: use tool_config instead
    tool_choice: Literal["auto", "required"]

    # DEPRECATED: use tool_config instead
    tool_prompt_format: Literal["json", "function_tag", "python_list"]

    toolgroups: List[Toolgroup]

    tool_config: ToolConfig

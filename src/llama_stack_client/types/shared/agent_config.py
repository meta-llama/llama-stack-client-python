# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..tool_def import ToolDef
from .response_format import ResponseFormat
from .sampling_params import SamplingParams

__all__ = ["AgentConfig", "Toolgroup", "ToolgroupUnionMember1"]


class ToolgroupUnionMember1(BaseModel):
    args: Dict[str, Union[bool, float, str, List[object], object, None]]

    name: str


Toolgroup: TypeAlias = Union[str, ToolgroupUnionMember1]


class AgentConfig(BaseModel):
    enable_session_persistence: bool

    instructions: str

    max_infer_iters: int

    model: str

    client_tools: Optional[List[ToolDef]] = None

    input_shields: Optional[List[str]] = None

    output_shields: Optional[List[str]] = None

    response_format: Optional[ResponseFormat] = None

    sampling_params: Optional[SamplingParams] = None

    tool_choice: Optional[Literal["auto", "required"]] = None

    tool_prompt_format: Optional[Literal["json", "function_tag", "python_list"]] = None

    toolgroups: Optional[List[Toolgroup]] = None

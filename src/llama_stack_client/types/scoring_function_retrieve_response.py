# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ScoringFunctionRetrieveResponse",
    "Parameter",
    "ParameterType",
    "ParameterTypeType",
    "ReturnType",
    "ReturnTypeType",
    "Context",
]


class ParameterTypeType(BaseModel):
    type: Literal["string"]


ParameterType: TypeAlias = Union[
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
]


class Parameter(BaseModel):
    name: str

    type: ParameterType

    description: Optional[str] = None


class ReturnTypeType(BaseModel):
    type: Literal["string"]


ReturnType: TypeAlias = Union[
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
]


class Context(BaseModel):
    judge_model: str

    judge_score_regex: Optional[List[str]] = None

    prompt_template: Optional[str] = None


class ScoringFunctionRetrieveResponse(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    parameters: List[Parameter]

    provider_id: str

    return_type: ReturnType

    context: Optional[Context] = None

    description: Optional[str] = None

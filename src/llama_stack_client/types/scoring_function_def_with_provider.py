# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ScoringFunctionDefWithProvider",
    "Parameter",
    "ParameterType",
    "ParameterTypeType",
    "ParameterTypeUnionMember7",
    "ReturnType",
    "ReturnTypeType",
    "ReturnTypeUnionMember7",
    "Context",
]


class ParameterTypeType(BaseModel):
    type: Literal["string"]


class ParameterTypeUnionMember7(BaseModel):
    type: Literal["custom"]

    validator_class: str


ParameterType: TypeAlias = Union[
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeType,
    ParameterTypeUnionMember7,
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


class ReturnTypeUnionMember7(BaseModel):
    type: Literal["custom"]

    validator_class: str


ReturnType: TypeAlias = Union[
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeUnionMember7,
    ReturnTypeType,
    ReturnTypeType,
    ReturnTypeType,
]


class Context(BaseModel):
    judge_model: str

    prompt_template: Optional[str] = None


class ScoringFunctionDefWithProvider(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    parameters: List[Parameter]

    provider_id: str

    return_type: ReturnType

    context: Optional[Context] = None

    description: Optional[str] = None

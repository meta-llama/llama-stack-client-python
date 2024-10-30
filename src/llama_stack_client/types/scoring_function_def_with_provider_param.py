# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ScoringFunctionDefWithProviderParam",
    "Parameter",
    "ParameterType",
    "ParameterTypeType",
    "ParameterTypeUnionMember7",
    "ReturnType",
    "ReturnTypeType",
    "ReturnTypeUnionMember7",
    "Context",
]


class ParameterTypeType(TypedDict, total=False):
    type: Required[Literal["string"]]


class ParameterTypeUnionMember7(TypedDict, total=False):
    type: Required[Literal["custom"]]

    validator_class: Required[str]


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


class Parameter(TypedDict, total=False):
    name: Required[str]

    type: Required[ParameterType]

    description: str


class ReturnTypeType(TypedDict, total=False):
    type: Required[Literal["string"]]


class ReturnTypeUnionMember7(TypedDict, total=False):
    type: Required[Literal["custom"]]

    validator_class: Required[str]


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


class Context(TypedDict, total=False):
    judge_model: Required[str]

    prompt_template: str


class ScoringFunctionDefWithProviderParam(TypedDict, total=False):
    identifier: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    parameters: Required[Iterable[Parameter]]

    provider_id: Required[str]

    return_type: Required[ReturnType]

    context: Context

    description: str

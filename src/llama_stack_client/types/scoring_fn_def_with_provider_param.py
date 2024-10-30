# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ScoringFnDefWithProviderParam",
    "Parameter",
    "ParameterType",
    "ParameterTypeType",
    "ReturnType",
    "ReturnTypeType",
    "Context",
]


class ParameterTypeType(TypedDict, total=False):
    type: Required[Literal["string"]]


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


class Parameter(TypedDict, total=False):
    name: Required[str]

    type: Required[ParameterType]

    description: str


class ReturnTypeType(TypedDict, total=False):
    type: Required[Literal["string"]]


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


class Context(TypedDict, total=False):
    judge_model: Required[str]

    judge_score_regex: List[str]

    prompt_template: str


class ScoringFnDefWithProviderParam(TypedDict, total=False):
    identifier: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    parameters: Required[Iterable[Parameter]]

    provider_id: Required[str]

    return_type: Required[ReturnType]

    context: Context

    description: str

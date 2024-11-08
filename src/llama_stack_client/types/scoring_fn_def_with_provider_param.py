# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ScoringFnDefWithProviderParam",
    "ReturnType",
    "ReturnTypeType",
    "Params",
    "ParamsLlmAsJudgeScoringFnParams",
    "ParamsRegexParserScoringFnParams",
]


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


class ParamsLlmAsJudgeScoringFnParams(TypedDict, total=False):
    judge_model: Required[str]

    type: Required[Literal["llm_as_judge"]]

    judge_score_regexes: List[str]

    prompt_template: str


class ParamsRegexParserScoringFnParams(TypedDict, total=False):
    type: Required[Literal["regex_parser"]]

    parsing_regexes: List[str]


Params: TypeAlias = Union[ParamsLlmAsJudgeScoringFnParams, ParamsRegexParserScoringFnParams]


class ScoringFnDefWithProviderParam(TypedDict, total=False):
    identifier: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    provider_id: Required[str]

    return_type: Required[ReturnType]

    type: Required[Literal["scoring_fn"]]

    description: str

    params: Params

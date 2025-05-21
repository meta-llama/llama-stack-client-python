# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ScoringFnParamsParam", "LlmAsJudgeScoringFnParams", "RegexParserScoringFnParams", "BasicScoringFnParams"]


class LlmAsJudgeScoringFnParams(TypedDict, total=False):
    aggregation_functions: Required[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ]

    judge_model: Required[str]

    judge_score_regexes: Required[List[str]]

    type: Required[Literal["llm_as_judge"]]

    prompt_template: str


class RegexParserScoringFnParams(TypedDict, total=False):
    aggregation_functions: Required[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ]

    parsing_regexes: Required[List[str]]

    type: Required[Literal["regex_parser"]]


class BasicScoringFnParams(TypedDict, total=False):
    aggregation_functions: Required[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ]

    type: Required[Literal["basic"]]


ScoringFnParamsParam: TypeAlias = Union[LlmAsJudgeScoringFnParams, RegexParserScoringFnParams, BasicScoringFnParams]

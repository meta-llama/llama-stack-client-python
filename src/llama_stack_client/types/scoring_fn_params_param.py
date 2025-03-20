# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ScoringFnParamsParam", "LlmAsJudgeScoringFnParams", "RegexParserScoringFnParams", "BasicScoringFnParams"]


class LlmAsJudgeScoringFnParams(TypedDict, total=False):
    judge_model: Required[str]

    type: Required[Literal["llm_as_judge"]]

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]

    judge_score_regexes: List[str]

    prompt_template: str


class RegexParserScoringFnParams(TypedDict, total=False):
    type: Required[Literal["regex_parser"]]

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]

    parsing_regexes: List[str]


class BasicScoringFnParams(TypedDict, total=False):
    type: Required[Literal["basic"]]

    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]


ScoringFnParamsParam: TypeAlias = Union[LlmAsJudgeScoringFnParams, RegexParserScoringFnParams, BasicScoringFnParams]

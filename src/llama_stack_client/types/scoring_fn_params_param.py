# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

from .scoring_fn_params_type import ScoringFnParamsType
from .aggregation_function_type import AggregationFunctionType

__all__ = ["ScoringFnParamsParam", "LlmAsJudgeScoringFnParams", "RegexParserScoringFnParams", "BasicScoringFnParams"]


class LlmAsJudgeScoringFnParams(TypedDict, total=False):
    aggregation_functions: Required[List[AggregationFunctionType]]

    judge_model: Required[str]

    judge_score_regexes: Required[List[str]]

    type: Required[ScoringFnParamsType]

    prompt_template: str


class RegexParserScoringFnParams(TypedDict, total=False):
    aggregation_functions: Required[List[AggregationFunctionType]]

    parsing_regexes: Required[List[str]]

    type: Required[ScoringFnParamsType]


class BasicScoringFnParams(TypedDict, total=False):
    aggregation_functions: Required[List[AggregationFunctionType]]

    type: Required[ScoringFnParamsType]


ScoringFnParamsParam: TypeAlias = Union[LlmAsJudgeScoringFnParams, RegexParserScoringFnParams, BasicScoringFnParams]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .scoring_fn_params_type import ScoringFnParamsType
from .aggregation_function_type import AggregationFunctionType

__all__ = ["ScoringFnParams", "LlmAsJudgeScoringFnParams", "RegexParserScoringFnParams", "BasicScoringFnParams"]


class LlmAsJudgeScoringFnParams(BaseModel):
    aggregation_functions: List[AggregationFunctionType]

    judge_model: str

    judge_score_regexes: List[str]

    type: ScoringFnParamsType

    prompt_template: Optional[str] = None


class RegexParserScoringFnParams(BaseModel):
    aggregation_functions: List[AggregationFunctionType]

    parsing_regexes: List[str]

    type: ScoringFnParamsType


class BasicScoringFnParams(BaseModel):
    aggregation_functions: List[AggregationFunctionType]

    type: ScoringFnParamsType


ScoringFnParams: TypeAlias = Union[LlmAsJudgeScoringFnParams, RegexParserScoringFnParams, BasicScoringFnParams]

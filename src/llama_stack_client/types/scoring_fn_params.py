# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["ScoringFnParams", "LlmAsJudgeScoringFnParams", "RegexParserScoringFnParams", "BasicScoringFnParams"]


class LlmAsJudgeScoringFnParams(BaseModel):
    judge_model: str

    type: Literal["llm_as_judge"]

    aggregation_functions: Optional[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ] = None

    judge_score_regexes: Optional[List[str]] = None

    prompt_template: Optional[str] = None


class RegexParserScoringFnParams(BaseModel):
    type: Literal["regex_parser"]

    aggregation_functions: Optional[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ] = None

    parsing_regexes: Optional[List[str]] = None


class BasicScoringFnParams(BaseModel):
    type: Literal["basic"]

    aggregation_functions: Optional[
        List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]
    ] = None


ScoringFnParams: TypeAlias = Annotated[
    Union[LlmAsJudgeScoringFnParams, RegexParserScoringFnParams, BasicScoringFnParams],
    PropertyInfo(discriminator="type"),
]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["ScoringFnParams", "LlmAsJudgeScoringFnParams", "RegexParserScoringFnParams", "BasicScoringFnParams"]


class LlmAsJudgeScoringFnParams(BaseModel):
    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]

    judge_model: str

    judge_score_regexes: List[str]

    type: Literal["llm_as_judge"]

    prompt_template: Optional[str] = None


class RegexParserScoringFnParams(BaseModel):
    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]

    parsing_regexes: List[str]

    type: Literal["regex_parser"]


class BasicScoringFnParams(BaseModel):
    aggregation_functions: List[Literal["average", "weighted_average", "median", "categorical_count", "accuracy"]]

    type: Literal["basic"]


ScoringFnParams: TypeAlias = Annotated[
    Union[LlmAsJudgeScoringFnParams, RegexParserScoringFnParams, BasicScoringFnParams],
    PropertyInfo(discriminator="type"),
]

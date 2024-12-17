# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.return_type import ReturnType

__all__ = [
    "ScoringFn",
    "Params",
    "ParamsLlmAsJudgeScoringFnParams",
    "ParamsRegexParserScoringFnParams",
    "ParamsBasicScoringFnParams",
]


class ParamsLlmAsJudgeScoringFnParams(BaseModel):
    judge_model: str

    type: Literal["llm_as_judge"]

    aggregation_functions: Optional[List[Literal["average", "median", "categorical_count", "accuracy"]]] = None

    judge_score_regexes: Optional[List[str]] = None

    prompt_template: Optional[str] = None


class ParamsRegexParserScoringFnParams(BaseModel):
    type: Literal["regex_parser"]

    aggregation_functions: Optional[List[Literal["average", "median", "categorical_count", "accuracy"]]] = None

    parsing_regexes: Optional[List[str]] = None


class ParamsBasicScoringFnParams(BaseModel):
    type: Literal["basic"]

    aggregation_functions: Optional[List[Literal["average", "median", "categorical_count", "accuracy"]]] = None


Params: TypeAlias = Union[ParamsLlmAsJudgeScoringFnParams, ParamsRegexParserScoringFnParams, ParamsBasicScoringFnParams]


class ScoringFn(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    provider_resource_id: str

    return_type: ReturnType

    type: Literal["scoring_function"]

    description: Optional[str] = None

    params: Optional[Params] = None

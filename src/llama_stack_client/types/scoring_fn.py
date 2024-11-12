# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ScoringFn",
    "ReturnType",
    "ReturnTypeType",
    "Params",
    "ParamsLlmAsJudgeScoringFnParams",
    "ParamsRegexParserScoringFnParams",
]


class ReturnTypeType(BaseModel):
    type: Literal["string"]


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


class ParamsLlmAsJudgeScoringFnParams(BaseModel):
    judge_model: str

    type: Literal["llm_as_judge"]

    judge_score_regexes: Optional[List[str]] = None

    prompt_template: Optional[str] = None


class ParamsRegexParserScoringFnParams(BaseModel):
    type: Literal["regex_parser"]

    parsing_regexes: Optional[List[str]] = None


Params: TypeAlias = Union[ParamsLlmAsJudgeScoringFnParams, ParamsRegexParserScoringFnParams]


class ScoringFn(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    provider_resource_id: str

    return_type: ReturnType

    type: Literal["scoring_function"]

    description: Optional[str] = None

    params: Optional[Params] = None

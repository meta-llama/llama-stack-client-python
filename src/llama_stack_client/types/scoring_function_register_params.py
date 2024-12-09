# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.return_type import ReturnType

__all__ = [
    "ScoringFunctionRegisterParams",
    "Params",
    "ParamsLlmAsJudgeScoringFnParams",
    "ParamsRegexParserScoringFnParams",
]


class ScoringFunctionRegisterParams(TypedDict, total=False):
    description: Required[str]

    return_type: Required[ReturnType]

    scoring_fn_id: Required[str]

    params: Params

    provider_id: str

    provider_scoring_fn_id: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class ParamsLlmAsJudgeScoringFnParams(TypedDict, total=False):
    judge_model: Required[str]

    type: Required[Literal["llm_as_judge"]]

    judge_score_regexes: List[str]

    prompt_template: str


class ParamsRegexParserScoringFnParams(TypedDict, total=False):
    type: Required[Literal["regex_parser"]]

    parsing_regexes: List[str]


Params: TypeAlias = Union[ParamsLlmAsJudgeScoringFnParams, ParamsRegexParserScoringFnParams]

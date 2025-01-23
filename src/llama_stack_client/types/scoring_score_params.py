# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ScoringScoreParams",
    "ScoringFunctions",
    "ScoringFunctionsLlmAsJudge",
    "ScoringFunctionsRegexParser",
    "ScoringFunctionsBasic",
]


class ScoringScoreParams(TypedDict, total=False):
    input_rows: Required[Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]]

    scoring_functions: Required[Dict[str, Optional[ScoringFunctions]]]

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]


class ScoringFunctionsLlmAsJudge(TypedDict, total=False):
    judge_model: Required[str]

    type: Required[Literal["llm_as_judge"]]

    aggregation_functions: List[Literal["average", "median", "categorical_count", "accuracy"]]

    judge_score_regexes: List[str]

    prompt_template: str


class ScoringFunctionsRegexParser(TypedDict, total=False):
    type: Required[Literal["regex_parser"]]

    aggregation_functions: List[Literal["average", "median", "categorical_count", "accuracy"]]

    parsing_regexes: List[str]


class ScoringFunctionsBasic(TypedDict, total=False):
    type: Required[Literal["basic"]]

    aggregation_functions: List[Literal["average", "median", "categorical_count", "accuracy"]]


ScoringFunctions: TypeAlias = Union[ScoringFunctionsLlmAsJudge, ScoringFunctionsRegexParser, ScoringFunctionsBasic]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "ScoringScoreParams",
    "ScoringFunctions",
    "ScoringFunctionsLlmAsJudgeScoringFnParams",
    "ScoringFunctionsRegexParserScoringFnParams",
]


class ScoringScoreParams(TypedDict, total=False):
    input_rows: Required[Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]]

    scoring_functions: Required[Dict[str, Optional[ScoringFunctions]]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class ScoringFunctionsLlmAsJudgeScoringFnParams(TypedDict, total=False):
    judge_model: Required[str]

    type: Required[Literal["llm_as_judge"]]

    judge_score_regexes: List[str]

    prompt_template: str


class ScoringFunctionsRegexParserScoringFnParams(TypedDict, total=False):
    type: Required[Literal["regex_parser"]]

    parsing_regexes: List[str]


ScoringFunctions: TypeAlias = Union[
    ScoringFunctionsLlmAsJudgeScoringFnParams, ScoringFunctionsRegexParserScoringFnParams
]

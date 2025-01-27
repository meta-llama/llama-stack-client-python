# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .eval_candidate_param import EvalCandidateParam
from .scoring_fn_params_param import ScoringFnParamsParam

__all__ = ["EvalTaskConfigParam", "BenchmarkEvalTaskConfig", "AppEvalTaskConfig"]


class BenchmarkEvalTaskConfig(TypedDict, total=False):
    eval_candidate: Required[EvalCandidateParam]

    type: Required[Literal["benchmark"]]

    num_examples: int


class AppEvalTaskConfig(TypedDict, total=False):
    eval_candidate: Required[EvalCandidateParam]

    scoring_params: Required[Dict[str, ScoringFnParamsParam]]

    type: Required[Literal["app"]]

    num_examples: int


EvalTaskConfigParam: TypeAlias = Union[BenchmarkEvalTaskConfig, AppEvalTaskConfig]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .eval_candidate_param import EvalCandidateParam
from .scoring_fn_params_param import ScoringFnParamsParam

__all__ = ["EvalTaskConfigParam"]


class EvalTaskConfigParam(TypedDict, total=False):
    eval_candidate: Required[EvalCandidateParam]

    scoring_params: Required[Dict[str, ScoringFnParamsParam]]

    type: Required[Literal["benchmark"]]

    num_examples: int

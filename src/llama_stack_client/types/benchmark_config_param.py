# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .eval_candidate_param import EvalCandidateParam
from .scoring_fn_params_param import ScoringFnParamsParam

__all__ = ["BenchmarkConfigParam"]


class BenchmarkConfigParam(TypedDict, total=False):
    eval_candidate: Required[EvalCandidateParam]
    """The candidate to evaluate."""

    scoring_params: Required[Dict[str, ScoringFnParamsParam]]
    """
    Map between scoring function id and parameters for each scoring function you
    want to run
    """

    num_examples: int
    """(Optional) The number of examples to evaluate.

    If not provided, all examples in the dataset will be evaluated
    """

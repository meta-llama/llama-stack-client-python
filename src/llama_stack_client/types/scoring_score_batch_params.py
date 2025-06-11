# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .scoring_fn_params_param import ScoringFnParamsParam

__all__ = ["ScoringScoreBatchParams"]


class ScoringScoreBatchParams(TypedDict, total=False):
    dataset_id: Required[str]

    save_results_dataset: Required[bool]

    scoring_functions: Required[Dict[str, Optional[ScoringFnParamsParam]]]

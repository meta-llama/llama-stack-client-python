# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .param_type_param import ParamTypeParam
from .scoring_fn_params_param import ScoringFnParamsParam

__all__ = ["ScoringFunctionCreateParams"]


class ScoringFunctionCreateParams(TypedDict, total=False):
    description: Required[str]

    return_type: Required[ParamTypeParam]

    scoring_fn_id: Required[str]

    params: ScoringFnParamsParam

    provider_id: str

    provider_scoring_fn_id: str

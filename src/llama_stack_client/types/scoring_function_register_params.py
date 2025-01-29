# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .scoring_fn_params_param import ScoringFnParamsParam
from .shared_params.return_type import ReturnType

__all__ = ["ScoringFunctionRegisterParams"]


class ScoringFunctionRegisterParams(TypedDict, total=False):
    description: Required[str]

    return_type: Required[ReturnType]

    scoring_fn_id: Required[str]

    params: ScoringFnParamsParam

    provider_id: str

    provider_scoring_fn_id: str

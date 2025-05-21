# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .scoring_fn_params_param import ScoringFnParamsParam
from .shared_params.return_type import ReturnType

__all__ = ["ScoringFunctionRegisterParams"]


class ScoringFunctionRegisterParams(TypedDict, total=False):
    description: Required[str]
    """The description of the scoring function."""

    return_type: Required[ReturnType]

    scoring_fn_id: Required[str]
    """The ID of the scoring function to register."""

    params: ScoringFnParamsParam
    """
    The parameters for the scoring function for benchmark eval, these can be
    overridden for app eval.
    """

    provider_id: str
    """The ID of the provider to use for the scoring function."""

    provider_scoring_fn_id: str
    """The ID of the provider scoring function to use for the scoring function."""

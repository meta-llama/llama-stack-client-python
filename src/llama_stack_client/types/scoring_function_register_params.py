# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .scoring_fn_def_with_provider_param import ScoringFnDefWithProviderParam

__all__ = ["ScoringFunctionRegisterParams"]


class ScoringFunctionRegisterParams(TypedDict, total=False):
    function_def: Required[ScoringFnDefWithProviderParam]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

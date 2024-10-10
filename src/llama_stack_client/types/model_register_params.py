# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .model_def_with_provider_param import ModelDefWithProviderParam

__all__ = ["ModelRegisterParams"]


class ModelRegisterParams(TypedDict, total=False):
    model: Required[ModelDefWithProviderParam]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

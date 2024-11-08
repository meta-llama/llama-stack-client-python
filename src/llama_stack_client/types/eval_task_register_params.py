# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .eval_task_def_with_provider_param import EvalTaskDefWithProviderParam

__all__ = ["EvalTaskRegisterParams"]


class EvalTaskRegisterParams(TypedDict, total=False):
    eval_task_def: Required[EvalTaskDefWithProviderParam]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

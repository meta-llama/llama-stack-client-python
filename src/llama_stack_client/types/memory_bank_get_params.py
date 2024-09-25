# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MemoryBankGetParams"]


class MemoryBankGetParams(TypedDict, total=False):
    bank_type: Required[Literal["vector", "keyvalue", "keyword", "graph"]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

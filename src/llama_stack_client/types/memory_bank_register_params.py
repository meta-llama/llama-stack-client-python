# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MemoryBankRegisterParams",
    "Params",
    "ParamsVectorMemoryBankParams",
    "ParamsKeyValueMemoryBankParams",
    "ParamsKeywordMemoryBankParams",
    "ParamsGraphMemoryBankParams",
]


class MemoryBankRegisterParams(TypedDict, total=False):
    memory_bank_id: Required[str]

    params: Required[Params]

    provider_id: str

    provider_memory_bank_id: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class ParamsVectorMemoryBankParams(TypedDict, total=False):
    chunk_size_in_tokens: Required[int]

    embedding_model: Required[str]

    memory_bank_type: Required[Literal["vector"]]

    overlap_size_in_tokens: int


class ParamsKeyValueMemoryBankParams(TypedDict, total=False):
    memory_bank_type: Required[Literal["keyvalue"]]


class ParamsKeywordMemoryBankParams(TypedDict, total=False):
    memory_bank_type: Required[Literal["keyword"]]


class ParamsGraphMemoryBankParams(TypedDict, total=False):
    memory_bank_type: Required[Literal["graph"]]


Params: TypeAlias = Union[
    ParamsVectorMemoryBankParams,
    ParamsKeyValueMemoryBankParams,
    ParamsKeywordMemoryBankParams,
    ParamsGraphMemoryBankParams,
]

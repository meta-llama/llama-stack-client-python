# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MemoryBankRegisterParams",
    "MemoryBank",
    "MemoryBankVectorMemoryBankDef",
    "MemoryBankKeyValueMemoryBankDef",
    "MemoryBankKeywordMemoryBankDef",
    "MemoryBankGraphMemoryBankDef",
]


class MemoryBankRegisterParams(TypedDict, total=False):
    memory_bank: Required[MemoryBank]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class MemoryBankVectorMemoryBankDef(TypedDict, total=False):
    chunk_size_in_tokens: Required[int]

    embedding_model: Required[str]

    identifier: Required[str]

    provider_id: Required[str]

    type: Required[Literal["vector"]]

    overlap_size_in_tokens: int


class MemoryBankKeyValueMemoryBankDef(TypedDict, total=False):
    identifier: Required[str]

    provider_id: Required[str]

    type: Required[Literal["keyvalue"]]


class MemoryBankKeywordMemoryBankDef(TypedDict, total=False):
    identifier: Required[str]

    provider_id: Required[str]

    type: Required[Literal["keyword"]]


class MemoryBankGraphMemoryBankDef(TypedDict, total=False):
    identifier: Required[str]

    provider_id: Required[str]

    type: Required[Literal["graph"]]


MemoryBank: TypeAlias = Union[
    MemoryBankVectorMemoryBankDef,
    MemoryBankKeyValueMemoryBankDef,
    MemoryBankKeywordMemoryBankDef,
    MemoryBankGraphMemoryBankDef,
]

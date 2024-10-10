# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MemoryCreateParams",
    "Config",
    "ConfigMemoryBankConfigVectorType",
    "ConfigMemoryBankConfigKeyValueType",
    "ConfigMemoryBankConfigKeywordType",
    "ConfigMemoryBankConfigGraphType",
]


class MemoryCreateParams(TypedDict, total=False):
    config: Required[Config]

    name: Required[str]

    url: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class ConfigMemoryBankConfigVectorType(TypedDict, total=False):
    chunk_size_in_tokens: Required[int]

    embedding_model: Required[str]

    type: Required[Literal["vector"]]

    overlap_size_in_tokens: int


class ConfigMemoryBankConfigKeyValueType(TypedDict, total=False):
    type: Required[Literal["keyvalue"]]


class ConfigMemoryBankConfigKeywordType(TypedDict, total=False):
    type: Required[Literal["keyword"]]


class ConfigMemoryBankConfigGraphType(TypedDict, total=False):
    type: Required[Literal["graph"]]


Config: TypeAlias = Union[
    ConfigMemoryBankConfigVectorType,
    ConfigMemoryBankConfigKeyValueType,
    ConfigMemoryBankConfigKeywordType,
    ConfigMemoryBankConfigGraphType,
]

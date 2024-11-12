# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "MemoryToolDefinition",
    "MemoryBankConfig",
    "MemoryBankConfigVector",
    "MemoryBankConfigKeyValue",
    "MemoryBankConfigKeyword",
    "MemoryBankConfigGraph",
    "QueryGeneratorConfig",
    "QueryGeneratorConfigDefault",
    "QueryGeneratorConfigLlm",
    "QueryGeneratorConfigCustom",
]


class MemoryBankConfigVector(TypedDict, total=False):
    bank_id: Required[str]

    type: Required[Literal["vector"]]


class MemoryBankConfigKeyValue(TypedDict, total=False):
    bank_id: Required[str]

    keys: Required[List[str]]

    type: Required[Literal["keyvalue"]]


class MemoryBankConfigKeyword(TypedDict, total=False):
    bank_id: Required[str]

    type: Required[Literal["keyword"]]


class MemoryBankConfigGraph(TypedDict, total=False):
    bank_id: Required[str]

    entities: Required[List[str]]

    type: Required[Literal["graph"]]


MemoryBankConfig: TypeAlias = Union[
    MemoryBankConfigVector, MemoryBankConfigKeyValue, MemoryBankConfigKeyword, MemoryBankConfigGraph
]


class QueryGeneratorConfigDefault(TypedDict, total=False):
    sep: Required[str]

    type: Required[Literal["default"]]


class QueryGeneratorConfigLlm(TypedDict, total=False):
    model: Required[str]

    template: Required[str]

    type: Required[Literal["llm"]]


class QueryGeneratorConfigCustom(TypedDict, total=False):
    type: Required[Literal["custom"]]


QueryGeneratorConfig: TypeAlias = Union[
    QueryGeneratorConfigDefault, QueryGeneratorConfigLlm, QueryGeneratorConfigCustom
]


class MemoryToolDefinition(TypedDict, total=False):
    max_chunks: Required[int]

    max_tokens_in_context: Required[int]

    memory_bank_configs: Required[Iterable[MemoryBankConfig]]

    query_generator_config: Required[QueryGeneratorConfig]

    type: Required[Literal["memory"]]

    input_shields: List[str]

    output_shields: List[str]

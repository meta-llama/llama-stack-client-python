# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

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


class MemoryBankConfigVector(BaseModel):
    bank_id: str

    type: Literal["vector"]


class MemoryBankConfigKeyValue(BaseModel):
    bank_id: str

    keys: List[str]

    type: Literal["keyvalue"]


class MemoryBankConfigKeyword(BaseModel):
    bank_id: str

    type: Literal["keyword"]


class MemoryBankConfigGraph(BaseModel):
    bank_id: str

    entities: List[str]

    type: Literal["graph"]


MemoryBankConfig: TypeAlias = Union[
    MemoryBankConfigVector, MemoryBankConfigKeyValue, MemoryBankConfigKeyword, MemoryBankConfigGraph
]


class QueryGeneratorConfigDefault(BaseModel):
    sep: str

    type: Literal["default"]


class QueryGeneratorConfigLlm(BaseModel):
    model: str

    template: str

    type: Literal["llm"]


class QueryGeneratorConfigCustom(BaseModel):
    type: Literal["custom"]


QueryGeneratorConfig: TypeAlias = Union[
    QueryGeneratorConfigDefault, QueryGeneratorConfigLlm, QueryGeneratorConfigCustom
]


class MemoryToolDefinition(BaseModel):
    max_chunks: int

    max_tokens_in_context: int

    memory_bank_configs: List[MemoryBankConfig]

    query_generator_config: QueryGeneratorConfig

    type: Literal["memory"]

    input_shields: Optional[List[str]] = None

    output_shields: Optional[List[str]] = None

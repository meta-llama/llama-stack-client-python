# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "MemoryBankRetrieveResponse",
    "VectorMemoryBankDef",
    "KeyValueMemoryBankDef",
    "KeywordMemoryBankDef",
    "GraphMemoryBankDef",
]


class VectorMemoryBankDef(BaseModel):
    chunk_size_in_tokens: int

    embedding_model: str

    identifier: str

    provider_id: str

    type: Literal["vector"]

    overlap_size_in_tokens: Optional[int] = None


class KeyValueMemoryBankDef(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["keyvalue"]


class KeywordMemoryBankDef(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["keyword"]


class GraphMemoryBankDef(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["graph"]


MemoryBankRetrieveResponse: TypeAlias = Union[
    VectorMemoryBankDef, KeyValueMemoryBankDef, KeywordMemoryBankDef, GraphMemoryBankDef, None
]

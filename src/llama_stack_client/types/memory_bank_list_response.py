# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["MemoryBankListResponse", "VectorMemoryBank", "KeyValueMemoryBank", "KeywordMemoryBank", "GraphMemoryBank"]


class VectorMemoryBank(BaseModel):
    chunk_size_in_tokens: int

    embedding_model: str

    identifier: str

    memory_bank_type: Literal["vector"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]

    overlap_size_in_tokens: Optional[int] = None


class KeyValueMemoryBank(BaseModel):
    identifier: str

    memory_bank_type: Literal["keyvalue"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]


class KeywordMemoryBank(BaseModel):
    identifier: str

    memory_bank_type: Literal["keyword"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]


class GraphMemoryBank(BaseModel):
    identifier: str

    memory_bank_type: Literal["graph"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]


MemoryBankListResponse: TypeAlias = Union[VectorMemoryBank, KeyValueMemoryBank, KeywordMemoryBank, GraphMemoryBank]

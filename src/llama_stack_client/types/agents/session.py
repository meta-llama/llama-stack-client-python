# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .turn import Turn
from ..._models import BaseModel

__all__ = [
    "Session",
    "MemoryBank",
    "MemoryBankVectorMemoryBank",
    "MemoryBankKeyValueMemoryBank",
    "MemoryBankKeywordMemoryBank",
    "MemoryBankGraphMemoryBank",
]


class MemoryBankVectorMemoryBank(BaseModel):
    chunk_size_in_tokens: int

    embedding_model: str

    identifier: str

    memory_bank_type: Literal["vector"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]

    overlap_size_in_tokens: Optional[int] = None


class MemoryBankKeyValueMemoryBank(BaseModel):
    identifier: str

    memory_bank_type: Literal["keyvalue"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]


class MemoryBankKeywordMemoryBank(BaseModel):
    identifier: str

    memory_bank_type: Literal["keyword"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]


class MemoryBankGraphMemoryBank(BaseModel):
    identifier: str

    memory_bank_type: Literal["graph"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]


MemoryBank: TypeAlias = Union[
    MemoryBankVectorMemoryBank, MemoryBankKeyValueMemoryBank, MemoryBankKeywordMemoryBank, MemoryBankGraphMemoryBank
]


class Session(BaseModel):
    session_id: str

    session_name: str

    started_at: datetime

    turns: List[Turn]

    memory_bank: Optional[MemoryBank] = None

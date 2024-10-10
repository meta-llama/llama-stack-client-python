# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .turn import Turn
from ..._models import BaseModel

__all__ = [
    "Session",
    "MemoryBank",
    "MemoryBankVectorMemoryBankDef",
    "MemoryBankKeyValueMemoryBankDef",
    "MemoryBankKeywordMemoryBankDef",
    "MemoryBankGraphMemoryBankDef",
]


class MemoryBankVectorMemoryBankDef(BaseModel):
    chunk_size_in_tokens: int

    embedding_model: str

    identifier: str

    provider_id: str

    type: Literal["vector"]

    overlap_size_in_tokens: Optional[int] = None


class MemoryBankKeyValueMemoryBankDef(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["keyvalue"]


class MemoryBankKeywordMemoryBankDef(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["keyword"]


class MemoryBankGraphMemoryBankDef(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["graph"]


MemoryBank: TypeAlias = Union[
    MemoryBankVectorMemoryBankDef,
    MemoryBankKeyValueMemoryBankDef,
    MemoryBankKeywordMemoryBankDef,
    MemoryBankGraphMemoryBankDef,
]


class Session(BaseModel):
    session_id: str

    session_name: str

    started_at: datetime

    turns: List[Turn]

    memory_bank: Optional[MemoryBank] = None

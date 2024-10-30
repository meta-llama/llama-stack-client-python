# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .turn import Turn
from ..._models import BaseModel
from ..shared.graph_memory_bank_def import GraphMemoryBankDef
from ..shared.vector_memory_bank_def import VectorMemoryBankDef
from ..shared.keyword_memory_bank_def import KeywordMemoryBankDef
from ..shared.key_value_memory_bank_def import KeyValueMemoryBankDef

__all__ = ["Session", "MemoryBank"]

MemoryBank: TypeAlias = Union[VectorMemoryBankDef, KeyValueMemoryBankDef, KeywordMemoryBankDef, GraphMemoryBankDef]


class Session(BaseModel):
    session_id: str

    session_name: str

    started_at: datetime

    turns: List[Turn]

    memory_bank: Optional[MemoryBank] = None

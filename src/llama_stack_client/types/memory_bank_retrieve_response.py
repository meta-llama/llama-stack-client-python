# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .shared.graph_memory_bank_def import GraphMemoryBankDef
from .shared.vector_memory_bank_def import VectorMemoryBankDef
from .shared.keyword_memory_bank_def import KeywordMemoryBankDef
from .shared.key_value_memory_bank_def import KeyValueMemoryBankDef

__all__ = ["MemoryBankRetrieveResponse"]

MemoryBankRetrieveResponse: TypeAlias = Union[
    VectorMemoryBankDef, KeyValueMemoryBankDef, KeywordMemoryBankDef, GraphMemoryBankDef, None
]

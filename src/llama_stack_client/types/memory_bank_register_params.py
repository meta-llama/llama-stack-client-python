# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.graph_memory_bank_def import GraphMemoryBankDef
from .shared_params.vector_memory_bank_def import VectorMemoryBankDef
from .shared_params.keyword_memory_bank_def import KeywordMemoryBankDef
from .shared_params.key_value_memory_bank_def import KeyValueMemoryBankDef

__all__ = ["MemoryBankRegisterParams", "MemoryBank"]


class MemoryBankRegisterParams(TypedDict, total=False):
    memory_bank: Required[MemoryBank]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


MemoryBank: TypeAlias = Union[VectorMemoryBankDef, KeyValueMemoryBankDef, KeywordMemoryBankDef, GraphMemoryBankDef]

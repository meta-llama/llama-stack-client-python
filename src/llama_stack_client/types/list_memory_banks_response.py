# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ListMemoryBanksResponse",
    "Data",
    "DataVectorMemoryBank",
    "DataKeyValueMemoryBank",
    "DataKeywordMemoryBank",
    "DataGraphMemoryBank",
]


class DataVectorMemoryBank(BaseModel):
    chunk_size_in_tokens: int

    embedding_model: str

    identifier: str

    memory_bank_type: Literal["vector"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]

    embedding_dimension: Optional[int] = None

    overlap_size_in_tokens: Optional[int] = None


class DataKeyValueMemoryBank(BaseModel):
    identifier: str

    memory_bank_type: Literal["keyvalue"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]


class DataKeywordMemoryBank(BaseModel):
    identifier: str

    memory_bank_type: Literal["keyword"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]


class DataGraphMemoryBank(BaseModel):
    identifier: str

    memory_bank_type: Literal["graph"]

    provider_id: str

    provider_resource_id: str

    type: Literal["memory_bank"]


Data: TypeAlias = Union[DataVectorMemoryBank, DataKeyValueMemoryBank, DataKeywordMemoryBank, DataGraphMemoryBank]


class ListMemoryBanksResponse(BaseModel):
    data: List[Data]

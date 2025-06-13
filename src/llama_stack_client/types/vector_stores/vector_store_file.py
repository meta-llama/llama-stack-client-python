# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "VectorStoreFile",
    "ChunkingStrategy",
    "ChunkingStrategyVectorStoreChunkingStrategyAuto",
    "ChunkingStrategyVectorStoreChunkingStrategyStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyStaticStatic",
    "LastError",
]


class ChunkingStrategyVectorStoreChunkingStrategyAuto(BaseModel):
    type: Literal["auto"]


class ChunkingStrategyVectorStoreChunkingStrategyStaticStatic(BaseModel):
    chunk_overlap_tokens: int

    max_chunk_size_tokens: int


class ChunkingStrategyVectorStoreChunkingStrategyStatic(BaseModel):
    static: ChunkingStrategyVectorStoreChunkingStrategyStaticStatic

    type: Literal["static"]


ChunkingStrategy: TypeAlias = Annotated[
    Union[ChunkingStrategyVectorStoreChunkingStrategyAuto, ChunkingStrategyVectorStoreChunkingStrategyStatic],
    PropertyInfo(discriminator="type"),
]


class LastError(BaseModel):
    code: Literal["server_error", "rate_limit_exceeded"]

    message: str


class VectorStoreFile(BaseModel):
    id: str

    attributes: Dict[str, Union[bool, float, str, List[object], object, None]]

    chunking_strategy: ChunkingStrategy

    created_at: int

    object: str

    status: Literal["completed", "in_progress", "cancelled", "failed"]

    usage_bytes: int

    vector_store_id: str

    last_error: Optional[LastError] = None

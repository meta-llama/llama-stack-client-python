# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "QueryDocuments",
    "Chunk",
    "ChunkContent",
    "ChunkContentImageMedia",
    "ChunkContentImageMediaImage",
    "ChunkContentImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "ChunkContentUnionMember2",
    "ChunkContentUnionMember2ImageMedia",
    "ChunkContentUnionMember2ImageMediaImage",
    "ChunkContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
]


class ChunkContentImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


ChunkContentImageMediaImage: TypeAlias = Union[ChunkContentImageMediaImageThisClassRepresentsAnImageObjectToCreate, str]


class ChunkContentImageMedia(BaseModel):
    image: ChunkContentImageMediaImage


class ChunkContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


ChunkContentUnionMember2ImageMediaImage: TypeAlias = Union[
    ChunkContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class ChunkContentUnionMember2ImageMedia(BaseModel):
    image: ChunkContentUnionMember2ImageMediaImage


ChunkContentUnionMember2: TypeAlias = Union[str, ChunkContentUnionMember2ImageMedia]

ChunkContent: TypeAlias = Union[str, ChunkContentImageMedia, List[ChunkContentUnionMember2]]


class Chunk(BaseModel):
    content: ChunkContent

    document_id: str

    token_count: int


class QueryDocuments(BaseModel):
    chunks: List[Chunk]

    scores: List[float]

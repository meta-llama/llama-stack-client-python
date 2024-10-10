# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.image_media import ImageMedia
from .shared.content_array import ContentArray

__all__ = ["QueryDocuments", "Chunk", "ChunkContent"]

ChunkContent: TypeAlias = Union[str, ImageMedia, ContentArray]


class Chunk(BaseModel):
    content: ChunkContent

    document_id: str

    token_count: int


class QueryDocuments(BaseModel):
    chunks: List[Chunk]

    scores: List[float]

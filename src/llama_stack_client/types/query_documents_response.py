# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.image_media import ImageMedia

__all__ = ["QueryDocumentsResponse", "Chunk", "ChunkContent", "ChunkContentImageMediaArray"]

ChunkContentImageMediaArray: TypeAlias = Union[str, ImageMedia]

ChunkContent: TypeAlias = Union[str, ImageMedia, List[ChunkContentImageMediaArray]]


class Chunk(BaseModel):
    content: ChunkContent

    document_id: str

    token_count: int


class QueryDocumentsResponse(BaseModel):
    chunks: List[Chunk]

    scores: List[float]

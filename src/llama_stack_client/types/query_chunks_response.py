# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel
from .shared.interleaved_content import InterleavedContent

__all__ = ["QueryChunksResponse", "Chunk"]


class Chunk(BaseModel):
    content: InterleavedContent
    """
    The content of the chunk, which can be interleaved text, images, or other types.
    """

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]
    """
    Metadata associated with the chunk, such as document ID, source, or other
    relevant information.
    """

    embedding: Optional[List[float]] = None
    """Optional embedding for the chunk. If not provided, it will be computed later."""


class QueryChunksResponse(BaseModel):
    chunks: List[Chunk]

    scores: List[float]

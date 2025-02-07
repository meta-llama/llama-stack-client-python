# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel
from .shared.interleaved_content import InterleavedContent

__all__ = ["QueryChunksResponse", "Chunk"]


class Chunk(BaseModel):
    content: InterleavedContent
    """A image content item"""

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]


class QueryChunksResponse(BaseModel):
    chunks: List[Chunk]

    scores: List[float]

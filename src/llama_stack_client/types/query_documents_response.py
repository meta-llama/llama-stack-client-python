# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.interleaved_content import InterleavedContent

__all__ = ["QueryDocumentsResponse", "Chunk"]


class Chunk(BaseModel):
    content: InterleavedContent

    document_id: str

    token_count: int


class QueryDocumentsResponse(BaseModel):
    chunks: List[Chunk]

    scores: List[float]

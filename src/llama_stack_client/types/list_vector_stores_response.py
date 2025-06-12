# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .vector_store import VectorStore

__all__ = ["ListVectorStoresResponse"]


class ListVectorStoresResponse(BaseModel):
    data: List[VectorStore]

    has_more: bool

    object: str

    first_id: Optional[str] = None

    last_id: Optional[str] = None

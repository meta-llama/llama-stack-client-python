# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..shared_params.query_config import QueryConfig
from ..shared_params.interleaved_content import InterleavedContent

__all__ = ["RagToolQueryParams"]


class RagToolQueryParams(TypedDict, total=False):
    content: Required[InterleavedContent]
    """A image content item"""

    vector_db_ids: Required[List[str]]

    query_config: QueryConfig
    """Configuration for the RAG query generation."""

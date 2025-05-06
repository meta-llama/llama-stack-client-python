# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .interleaved_content_param import InterleavedContentParam

__all__ = ["VectorIoInsertParams", "Chunk"]


class VectorIoInsertParams(TypedDict, total=False):
    chunks: Required[Iterable[Chunk]]

    vector_db_id: Required[str]

    ttl_seconds: int


class Chunk(TypedDict, total=False):
    content: Required[InterleavedContentParam]
    """A image content item"""

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

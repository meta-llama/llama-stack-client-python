# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.interleaved_content import InterleavedContent

__all__ = ["VectorIoInsertParams", "Chunk"]


class VectorIoInsertParams(TypedDict, total=False):
    chunks: Required[Iterable[Chunk]]
    """The chunks to insert.

    Each `Chunk` should contain content which can be interleaved text, images, or
    other types. `metadata`: `dict[str, Any]` and `embedding`: `List[float]` are
    optional. If `metadata` is provided, you configure how Llama Stack formats the
    chunk during generation. If `embedding` is not provided, it will be computed
    later.
    """

    vector_db_id: Required[str]
    """The identifier of the vector database to insert the chunks into."""

    ttl_seconds: int
    """The time to live of the chunks."""


class Chunk(TypedDict, total=False):
    content: Required[InterleavedContent]
    """
    The content of the chunk, which can be interleaved text, images, or other types.
    """

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """
    Metadata associated with the chunk, such as document ID, source, or other
    relevant information.
    """

    embedding: Iterable[float]
    """Optional embedding for the chunk. If not provided, it will be computed later."""

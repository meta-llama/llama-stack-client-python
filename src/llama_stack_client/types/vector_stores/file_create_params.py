# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "FileCreateParams",
    "ChunkingStrategy",
    "ChunkingStrategyVectorStoreChunkingStrategyAuto",
    "ChunkingStrategyVectorStoreChunkingStrategyStatic",
    "ChunkingStrategyVectorStoreChunkingStrategyStaticStatic",
]


class FileCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to attach to the vector store."""

    attributes: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """The key-value attributes stored with the file, which can be used for filtering."""

    chunking_strategy: ChunkingStrategy
    """The chunking strategy to use for the file."""


class ChunkingStrategyVectorStoreChunkingStrategyAuto(TypedDict, total=False):
    type: Required[Literal["auto"]]


class ChunkingStrategyVectorStoreChunkingStrategyStaticStatic(TypedDict, total=False):
    chunk_overlap_tokens: Required[int]

    max_chunk_size_tokens: Required[int]


class ChunkingStrategyVectorStoreChunkingStrategyStatic(TypedDict, total=False):
    static: Required[ChunkingStrategyVectorStoreChunkingStrategyStaticStatic]

    type: Required[Literal["static"]]


ChunkingStrategy: TypeAlias = Union[
    ChunkingStrategyVectorStoreChunkingStrategyAuto, ChunkingStrategyVectorStoreChunkingStrategyStatic
]

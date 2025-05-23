# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .query_generator_config import QueryGeneratorConfig

__all__ = ["QueryConfig"]


class QueryConfig(TypedDict, total=False):
    chunk_template: Required[str]
    """Template for formatting each retrieved chunk in the context.

    Available placeholders: {index} (1-based chunk ordinal), {chunk.content} (chunk
    content string), {metadata} (chunk metadata dict). Default: "Result
    {index}\nContent: {chunk.content}\nMetadata: {metadata}\n"
    """

    max_chunks: Required[int]
    """Maximum number of chunks to retrieve."""

    max_tokens_in_context: Required[int]
    """Maximum number of tokens in the context."""

    query_generator_config: Required[QueryGeneratorConfig]
    """Configuration for the query generator."""

    mode: str
    """Search mode for retrieval—either "vector" or "keyword". Default "vector"."""

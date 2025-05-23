# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .query_generator_config import QueryGeneratorConfig

__all__ = ["QueryConfig"]


class QueryConfig(BaseModel):
    chunk_template: str
    """Template for formatting each retrieved chunk in the context.

    Available placeholders: {index} (1-based chunk ordinal), {chunk.content} (chunk
    content string), {metadata} (chunk metadata dict). Default: "Result
    {index}\nContent: {chunk.content}\nMetadata: {metadata}\n"
    """

    max_chunks: int
    """Maximum number of chunks to retrieve."""

    max_tokens_in_context: int
    """Maximum number of tokens in the context."""

    query_generator_config: QueryGeneratorConfig
    """Configuration for the query generator."""

    mode: Optional[str] = None
    """Search mode for retrieval—either "vector" or "keyword". Default "vector"."""

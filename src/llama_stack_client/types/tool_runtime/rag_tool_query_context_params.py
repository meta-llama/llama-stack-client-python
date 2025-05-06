# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..interleaved_content_param import InterleavedContentParam

__all__ = [
    "RagToolQueryContextParams",
    "QueryConfig",
    "QueryConfigQueryGeneratorConfig",
    "QueryConfigQueryGeneratorConfigDefaultRagQueryGeneratorConfig",
    "QueryConfigQueryGeneratorConfigLlmragQueryGeneratorConfig",
]


class RagToolQueryContextParams(TypedDict, total=False):
    content: Required[InterleavedContentParam]
    """A image content item"""

    vector_db_ids: Required[List[str]]

    query_config: QueryConfig


class QueryConfigQueryGeneratorConfigDefaultRagQueryGeneratorConfig(TypedDict, total=False):
    separator: Required[str]

    type: Required[Literal["default"]]


class QueryConfigQueryGeneratorConfigLlmragQueryGeneratorConfig(TypedDict, total=False):
    model: Required[str]

    template: Required[str]

    type: Required[Literal["llm"]]


QueryConfigQueryGeneratorConfig: TypeAlias = Union[
    QueryConfigQueryGeneratorConfigDefaultRagQueryGeneratorConfig,
    QueryConfigQueryGeneratorConfigLlmragQueryGeneratorConfig,
]


class QueryConfig(TypedDict, total=False):
    max_chunks: Required[int]

    max_tokens_in_context: Required[int]

    query_generator_config: Required[QueryConfigQueryGeneratorConfig]

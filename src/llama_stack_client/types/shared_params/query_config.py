# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .query_generator_config import QueryGeneratorConfig

__all__ = ["QueryConfig"]


class QueryConfig(TypedDict, total=False):
    max_chunks: Required[int]

    max_tokens_in_context: Required[int]

    query_generator_config: Required[QueryGeneratorConfig]

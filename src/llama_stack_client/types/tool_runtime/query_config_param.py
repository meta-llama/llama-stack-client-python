# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "QueryConfigParam",
    "QueryGeneratorConfig",
    "QueryGeneratorConfigDefaultRagQueryGeneratorConfig",
    "QueryGeneratorConfigLlmragQueryGeneratorConfig",
]


class QueryGeneratorConfigDefaultRagQueryGeneratorConfig(TypedDict, total=False):
    separator: Required[str]

    type: Required[Literal["default"]]


class QueryGeneratorConfigLlmragQueryGeneratorConfig(TypedDict, total=False):
    model: Required[str]

    template: Required[str]

    type: Required[Literal["llm"]]


QueryGeneratorConfig: TypeAlias = Union[
    QueryGeneratorConfigDefaultRagQueryGeneratorConfig, QueryGeneratorConfigLlmragQueryGeneratorConfig
]


class QueryConfigParam(TypedDict, total=False):
    max_chunks: Required[int]

    max_tokens_in_context: Required[int]

    query_generator_config: Required[QueryGeneratorConfig]

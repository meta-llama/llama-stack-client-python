# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["QueryConfig", "QueryGeneratorConfig", "QueryGeneratorConfigDefault", "QueryGeneratorConfigLlm"]


class QueryGeneratorConfigDefault(TypedDict, total=False):
    separator: Required[str]

    type: Required[Literal["default"]]


class QueryGeneratorConfigLlm(TypedDict, total=False):
    model: Required[str]

    template: Required[str]

    type: Required[Literal["llm"]]


QueryGeneratorConfig: TypeAlias = Union[QueryGeneratorConfigDefault, QueryGeneratorConfigLlm]


class QueryConfig(TypedDict, total=False):
    max_chunks: Required[int]

    max_tokens_in_context: Required[int]

    query_generator_config: Required[QueryGeneratorConfig]

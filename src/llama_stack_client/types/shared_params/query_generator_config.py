# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["QueryGeneratorConfig", "DefaultRagQueryGeneratorConfig", "LlmragQueryGeneratorConfig"]


class DefaultRagQueryGeneratorConfig(TypedDict, total=False):
    separator: Required[str]

    type: Required[Literal["default"]]


class LlmragQueryGeneratorConfig(TypedDict, total=False):
    model: Required[str]

    template: Required[str]

    type: Required[Literal["llm"]]


QueryGeneratorConfig: TypeAlias = Union[DefaultRagQueryGeneratorConfig, LlmragQueryGeneratorConfig]

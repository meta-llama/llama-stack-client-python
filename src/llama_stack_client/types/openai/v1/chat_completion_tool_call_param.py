# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ChatCompletionToolCallParam", "Function"]


class Function(TypedDict, total=False):
    arguments: str

    name: str


class ChatCompletionToolCallParam(TypedDict, total=False):
    type: Required[Literal["function"]]

    id: str

    function: Function

    index: int

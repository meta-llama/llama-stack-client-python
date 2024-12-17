# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .tool_call import ToolCall
from .interleaved_content import InterleavedContent

__all__ = ["CompletionMessage"]


class CompletionMessage(TypedDict, total=False):
    content: Required[InterleavedContent]

    role: Required[Literal["assistant"]]

    stop_reason: Required[Literal["end_of_turn", "end_of_message", "out_of_tokens"]]

    tool_calls: Required[Iterable[ToolCall]]

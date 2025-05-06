# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...interleaved_content_param import InterleavedContentParam

__all__ = ["ToolResponseMessageParam"]


class ToolResponseMessageParam(TypedDict, total=False):
    call_id: Required[str]
    """Unique identifier for the tool call this response is for"""

    content: Required[InterleavedContentParam]
    """The response content from the tool"""

    role: Required[Literal["tool"]]
    """Must be "tool" to identify this as a tool response"""

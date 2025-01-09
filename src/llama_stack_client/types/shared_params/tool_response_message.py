# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from .interleaved_content import InterleavedContent

__all__ = ["ToolResponseMessage"]


class ToolResponseMessage(TypedDict, total=False):
    call_id: Required[str]

    content: Required[InterleavedContent]

    role: Required[Literal["ipython"]]

    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .interleaved_content import InterleavedContent

__all__ = ["SystemMessage"]


class SystemMessage(TypedDict, total=False):
    content: Required[InterleavedContent]

    role: Required[Literal["system"]]

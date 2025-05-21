# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ToolListParams"]


class ToolListParams(TypedDict, total=False):
    toolgroup_id: str
    """The ID of the tool group to list tools for."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .shared_params.url import URL

__all__ = ["ToolRuntimeListToolsParams"]


class ToolRuntimeListToolsParams(TypedDict, total=False):
    mcp_endpoint: URL

    tool_group_id: str

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolRuntimeListToolsParams", "McpEndpoint"]


class ToolRuntimeListToolsParams(TypedDict, total=False):
    mcp_endpoint: McpEndpoint

    tool_group_id: str


class McpEndpoint(TypedDict, total=False):
    uri: Required[str]

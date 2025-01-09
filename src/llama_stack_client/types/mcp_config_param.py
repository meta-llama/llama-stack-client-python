# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.url import URL

__all__ = ["McpConfigParam", "McpInlineConfig", "McpRemoteConfig"]


class McpInlineConfig(TypedDict, total=False):
    command: Required[str]

    type: Required[Literal["inline"]]

    args: List[str]

    env: Dict[str, Union[bool, float, str, Iterable[object], object, None]]


class McpRemoteConfig(TypedDict, total=False):
    mcp_endpoint: Required[URL]

    type: Required[Literal["remote"]]


McpConfigParam: TypeAlias = Union[McpInlineConfig, McpRemoteConfig]

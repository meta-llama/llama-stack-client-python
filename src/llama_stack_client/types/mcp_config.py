# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.url import URL

__all__ = ["McpConfig", "McpInlineConfig", "McpRemoteConfig"]


class McpInlineConfig(BaseModel):
    command: str

    type: Literal["inline"]

    args: Optional[List[str]] = None

    env: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class McpRemoteConfig(BaseModel):
    mcp_endpoint: URL

    type: Literal["remote"]


McpConfig: TypeAlias = Union[McpInlineConfig, McpRemoteConfig]

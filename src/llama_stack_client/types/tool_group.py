# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .shared.url import URL

__all__ = ["ToolGroup"]


class ToolGroup(BaseModel):
    identifier: str

    provider_id: str

    provider_resource_id: str

    type: Literal["tool_group"]

    args: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    mcp_endpoint: Optional[URL] = None
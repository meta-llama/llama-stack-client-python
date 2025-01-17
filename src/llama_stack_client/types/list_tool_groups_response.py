# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .tool_group import ToolGroup

__all__ = ["ListToolGroupsResponse"]


class ListToolGroupsResponse(BaseModel):
    data: List[ToolGroup]

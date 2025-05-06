# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .tool_def import ToolDef

__all__ = ["ToolRuntimeListToolsResponse"]


class ToolRuntimeListToolsResponse(BaseModel):
    data: List[ToolDef]

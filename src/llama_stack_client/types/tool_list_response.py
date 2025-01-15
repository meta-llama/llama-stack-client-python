# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .tool import Tool
from .._models import BaseModel

__all__ = ["ToolListResponse"]


class ToolListResponse(BaseModel):
    data: List[Tool]

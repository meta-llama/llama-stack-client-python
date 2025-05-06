# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel
from .tool_parameter import ToolParameter

__all__ = ["ToolDef"]


class ToolDef(BaseModel):
    name: str

    description: Optional[str] = None

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    parameters: Optional[List[ToolParameter]] = None

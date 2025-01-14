# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["ToolDef", "Parameter"]


class Parameter(BaseModel):
    description: str

    name: str

    parameter_type: str

    required: bool

    default: Union[bool, float, str, List[object], object, None] = None


class ToolDef(BaseModel):
    name: str

    description: Optional[str] = None

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    parameters: Optional[List[Parameter]] = None

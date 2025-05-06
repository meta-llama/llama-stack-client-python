# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .._models import BaseModel

__all__ = ["ToolParameter"]


class ToolParameter(BaseModel):
    description: str

    name: str

    parameter_type: str

    required: bool

    default: Union[bool, float, str, List[object], object, None] = None

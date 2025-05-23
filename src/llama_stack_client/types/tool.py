# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Tool", "Parameter"]


class Parameter(BaseModel):
    description: str

    name: str

    parameter_type: str

    required: bool

    default: Union[bool, float, str, List[object], object, None] = None


class Tool(BaseModel):
    description: str

    identifier: str

    parameters: List[Parameter]

    provider_id: str

    tool_host: Literal["distribution", "client", "model_context_protocol"]

    toolgroup_id: str

    type: Literal["tool"]

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    provider_resource_id: Optional[str] = None

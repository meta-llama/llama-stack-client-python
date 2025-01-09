# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .tool_param_definition import ToolParamDefinition
from .rest_api_execution_config import RestAPIExecutionConfig

__all__ = ["FunctionCallToolDefinition"]


class FunctionCallToolDefinition(BaseModel):
    description: str

    function_name: str

    parameters: Dict[str, ToolParamDefinition]

    type: Literal["function_call"]

    input_shields: Optional[List[str]] = None

    output_shields: Optional[List[str]] = None

    remote_execution: Optional[RestAPIExecutionConfig] = None

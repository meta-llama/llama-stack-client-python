# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from typing_extensions import Literal

from ..._models import BaseModel
from ..rest_api_execution_config_param import RestAPIExecutionConfigParam
from .tool_param_definition import ToolParamDefinition

__all__ = ["FunctionCallToolDefinition"]


class FunctionCallToolDefinition(BaseModel):
    description: str

    function_name: str

    parameters: Dict[str, ToolParamDefinition]

    type: Literal["function_call"]

    input_shields: Optional[List[str]] = None

    output_shields: Optional[List[str]] = None

    remote_execution: Optional[RestAPIExecutionConfigParam] = None

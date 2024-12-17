# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal, Required, TypedDict

from .tool_param_definition import ToolParamDefinition
from .rest_api_execution_config import RestAPIExecutionConfig

__all__ = ["FunctionCallToolDefinition"]


class FunctionCallToolDefinition(TypedDict, total=False):
    description: Required[str]

    function_name: Required[str]

    parameters: Required[Dict[str, ToolParamDefinition]]

    type: Required[Literal["function_call"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfig

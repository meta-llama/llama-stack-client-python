# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from ..rest_api_execution_config_param import RestAPIExecutionConfigParam

__all__ = ["CodeInterpreterToolDefinition"]


class CodeInterpreterToolDefinition(TypedDict, total=False):
    enable_inline_code_execution: Required[bool]

    type: Required[Literal["code_interpreter"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .tool_parameter_param import ToolParameterParam

__all__ = ["ToolDefParam"]


class ToolDefParam(TypedDict, total=False):
    name: Required[str]

    description: str

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    parameters: Iterable[ToolParameterParam]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ToolDefParam", "Parameter"]


class Parameter(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameter_type: Required[str]

    required: Required[bool]

    default: Union[bool, float, str, Iterable[object], object, None]


class ToolDefParam(TypedDict, total=False):
    name: Required[str]

    description: str

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    parameters: Iterable[Parameter]

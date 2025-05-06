# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ToolParameterParam"]


class ToolParameterParam(TypedDict, total=False):
    description: Required[str]

    name: Required[str]

    parameter_type: Required[str]

    required: Required[bool]

    default: Union[bool, float, str, Iterable[object], object, None]

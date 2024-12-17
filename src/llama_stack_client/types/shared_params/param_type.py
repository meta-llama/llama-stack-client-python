# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ParamType", "Type"]


class Type(TypedDict, total=False):
    type: Required[Literal["string"]]


ParamType: TypeAlias = Union[Type, Type, Type, Type, Type, Type, Type, Type, Type, Type]

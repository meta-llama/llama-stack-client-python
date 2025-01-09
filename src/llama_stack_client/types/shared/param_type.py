# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["ParamType", "Type"]


class Type(BaseModel):
    type: Literal["string"]


ParamType: TypeAlias = Union[Type, Type, Type, Type, Type, Type, Type, Type, Type, Type]

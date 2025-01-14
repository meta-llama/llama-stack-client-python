# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .tool_call import ToolCall

__all__ = ["ContentDelta", "UnionMember0", "UnionMember1", "ToolCallDelta", "ToolCallDeltaContent"]


class UnionMember0(BaseModel):
    text: str

    type: Literal["text"]


class UnionMember1(BaseModel):
    data: str

    type: Literal["image"]


ToolCallDeltaContent: TypeAlias = Union[str, ToolCall]


class ToolCallDelta(BaseModel):
    content: ToolCallDeltaContent

    parse_status: Literal["started", "in_progress", "failed", "succeeded"]

    type: Literal["tool_call"]


ContentDelta: TypeAlias = Union[UnionMember0, UnionMember1, ToolCallDelta]

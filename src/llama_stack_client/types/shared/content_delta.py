# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .tool_call import ToolCall

__all__ = ["ContentDelta", "TextDelta", "ImageDelta", "ToolCallDelta", "ToolCallDeltaContent"]


class TextDelta(BaseModel):
    text: str

    type: Literal["text"]


class ImageDelta(BaseModel):
    data: str

    type: Literal["image"]


ToolCallDeltaContent: TypeAlias = Union[str, ToolCall]


class ToolCallDelta(BaseModel):
    content: ToolCallDeltaContent

    parse_status: Literal["started", "in_progress", "failed", "succeeded"]

    type: Literal["tool_call"]


ContentDelta: TypeAlias = Union[TextDelta, ImageDelta, ToolCallDelta]

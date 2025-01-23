# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from . import tool_call
from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["ContentDelta", "Text", "Image", "ToolCall", "ToolCallToolCall"]


class Text(BaseModel):
    text: str

    type: Literal["text"]


class Image(BaseModel):
    image: str

    type: Literal["image"]


ToolCallToolCall: TypeAlias = Union[str, tool_call.ToolCall]


class ToolCall(BaseModel):
    parse_status: Literal["started", "in_progress", "failed", "succeeded"]

    tool_call: ToolCallToolCall

    type: Literal["tool_call"]


ContentDelta: TypeAlias = Annotated[Union[Text, Image, ToolCall], PropertyInfo(discriminator="type")]

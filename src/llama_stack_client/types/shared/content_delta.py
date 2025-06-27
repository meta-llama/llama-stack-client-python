# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from .tool_call_or_string import ToolCallOrString

__all__ = ["ContentDelta", "TextDelta", "ImageDelta", "ToolCallDelta"]


class TextDelta(BaseModel):
    text: str

    type: Literal["text"]


class ImageDelta(BaseModel):
    image: str

    type: Literal["image"]


class ToolCallDelta(BaseModel):
    parse_status: Literal["started", "in_progress", "failed", "succeeded"]

    tool_call: ToolCallOrString

    type: Literal["tool_call"]


ContentDelta: TypeAlias = Annotated[Union[TextDelta, ImageDelta, ToolCallDelta], PropertyInfo(discriminator="type")]

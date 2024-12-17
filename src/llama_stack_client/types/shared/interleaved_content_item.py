# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["InterleavedContentItem", "ImageContentItem", "TextContentItem"]


class ImageContentItem(BaseModel):
    data: str

    type: Literal["image"]


class TextContentItem(BaseModel):
    text: str

    type: Literal["text"]


InterleavedContentItem: TypeAlias = Union[ImageContentItem, TextContentItem]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["InterleavedContentItem", "ImageContentItem", "TextContentItem"]


class ImageContentItem(BaseModel):
    type: Literal["image"]

    data: Optional[str] = None

    url: Optional[str] = None


class TextContentItem(BaseModel):
    text: str

    type: Literal["text"]


InterleavedContentItem: TypeAlias = Union[ImageContentItem, TextContentItem]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .url import URL
from ..._models import BaseModel

__all__ = ["InterleavedContentItem", "ImageContentItem", "TextContentItem"]


class ImageContentItem(BaseModel):
    type: Literal["image"]

    data: Optional[str] = None

    url: Optional[URL] = None


class TextContentItem(BaseModel):
    text: str

    type: Literal["text"]


InterleavedContentItem: TypeAlias = Union[ImageContentItem, TextContentItem]

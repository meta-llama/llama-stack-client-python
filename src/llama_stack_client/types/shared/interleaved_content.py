# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .url import URL
from ..._models import BaseModel
from .interleaved_content_item import InterleavedContentItem

__all__ = ["InterleavedContent", "ImageContentItem", "ImageContentItemImage", "TextContentItem"]


class ImageContentItemImage(BaseModel):
    data: Optional[str] = None

    url: Optional[URL] = None


class ImageContentItem(BaseModel):
    image: ImageContentItemImage

    type: Literal["image"]


class TextContentItem(BaseModel):
    text: str

    type: Literal["text"]


InterleavedContent: TypeAlias = Union[str, ImageContentItem, TextContentItem, List[InterleavedContentItem]]

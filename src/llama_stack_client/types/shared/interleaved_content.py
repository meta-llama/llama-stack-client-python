# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .url import URL
from ..._models import BaseModel
from .interleaved_content_item import InterleavedContentItem

__all__ = ["InterleavedContent", "ImageContentItem", "TextContentItem"]


class ImageContentItem(BaseModel):
    type: Literal["image"]

    data: Optional[str] = None

    url: Optional[URL] = None


class TextContentItem(BaseModel):
    text: str

    type: Literal["text"]


InterleavedContent: TypeAlias = Union[str, ImageContentItem, TextContentItem, List[InterleavedContentItem]]

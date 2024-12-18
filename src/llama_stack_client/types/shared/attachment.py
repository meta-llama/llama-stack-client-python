# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .url import URL
from ..._models import BaseModel
from .interleaved_content_item import InterleavedContentItem

__all__ = ["Attachment", "Content", "ContentImageContentItem", "ContentTextContentItem"]


class ContentImageContentItem(BaseModel):
    type: Literal["image"]

    data: Optional[str] = None

    url: Optional[URL] = None


class ContentTextContentItem(BaseModel):
    text: str

    type: Literal["text"]


Content: TypeAlias = Union[str, ContentImageContentItem, ContentTextContentItem, List[InterleavedContentItem], URL]


class Attachment(BaseModel):
    content: Content

    mime_type: str

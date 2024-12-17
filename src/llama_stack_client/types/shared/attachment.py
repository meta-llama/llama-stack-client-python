# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .interleaved_content_item import InterleavedContentItem

__all__ = ["Attachment", "Content", "ContentImageContentItem", "ContentTextContentItem"]


class ContentImageContentItem(BaseModel):
    data: str

    type: Literal["image"]


class ContentTextContentItem(BaseModel):
    text: str

    type: Literal["text"]


Content: TypeAlias = Union[str, ContentImageContentItem, ContentTextContentItem, List[InterleavedContentItem]]


class Attachment(BaseModel):
    content: Content

    mime_type: str

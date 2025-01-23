# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .url import URL
from ..._models import BaseModel
from .interleaved_content_item import InterleavedContentItem

__all__ = ["Document", "Content", "ContentImageContentItem", "ContentImageContentItemImage", "ContentTextContentItem"]


class ContentImageContentItemImage(BaseModel):
    data: Optional[str] = None

    url: Optional[URL] = None


class ContentImageContentItem(BaseModel):
    image: ContentImageContentItemImage

    type: Literal["image"]


class ContentTextContentItem(BaseModel):
    text: str

    type: Literal["text"]


Content: TypeAlias = Union[str, ContentImageContentItem, ContentTextContentItem, List[InterleavedContentItem], URL]


class Document(BaseModel):
    content: Content

    document_id: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    mime_type: Optional[str] = None

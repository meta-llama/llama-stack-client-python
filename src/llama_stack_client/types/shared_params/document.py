# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .url import URL
from .interleaved_content_item import InterleavedContentItem

__all__ = ["Document", "Content", "ContentImageContentItem", "ContentImageContentItemImage", "ContentTextContentItem"]


class ContentImageContentItemImage(TypedDict, total=False):
    data: str

    url: URL


class ContentImageContentItem(TypedDict, total=False):
    image: Required[ContentImageContentItemImage]

    type: Required[Literal["image"]]


class ContentTextContentItem(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


Content: TypeAlias = Union[str, ContentImageContentItem, ContentTextContentItem, Iterable[InterleavedContentItem], URL]


class Document(TypedDict, total=False):
    content: Required[Content]

    document_id: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    mime_type: str

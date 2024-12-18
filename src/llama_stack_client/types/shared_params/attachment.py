# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .url import URL
from .interleaved_content_item import InterleavedContentItem

__all__ = ["Attachment", "Content", "ContentImageContentItem", "ContentTextContentItem"]


class ContentImageContentItem(TypedDict, total=False):
    type: Required[Literal["image"]]

    data: str

    url: URL


class ContentTextContentItem(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


Content: TypeAlias = Union[str, ContentImageContentItem, ContentTextContentItem, Iterable[InterleavedContentItem], URL]


class Attachment(TypedDict, total=False):
    content: Required[Content]

    mime_type: Required[str]

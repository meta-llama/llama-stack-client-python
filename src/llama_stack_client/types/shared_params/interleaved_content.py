# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .url import URL
from .interleaved_content_item import InterleavedContentItem

__all__ = ["InterleavedContent", "ImageContentItem", "ImageContentItemImage", "TextContentItem"]


class ImageContentItemImage(TypedDict, total=False):
    data: str

    url: URL


class ImageContentItem(TypedDict, total=False):
    image: Required[ImageContentItemImage]

    type: Required[Literal["image"]]


class TextContentItem(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


InterleavedContent: TypeAlias = Union[str, ImageContentItem, TextContentItem, Iterable[InterleavedContentItem]]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .url import URL

__all__ = ["InterleavedContentItem", "ImageContentItem", "ImageContentItemImage", "TextContentItem"]


class ImageContentItemImage(TypedDict, total=False):
    data: str

    url: URL


class ImageContentItem(TypedDict, total=False):
    image: Required[ImageContentItemImage]

    type: Required[Literal["image"]]


class TextContentItem(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


InterleavedContentItem: TypeAlias = Union[ImageContentItem, TextContentItem]

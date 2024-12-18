# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .url import URL

__all__ = ["InterleavedContentItem", "ImageContentItem", "TextContentItem"]


class ImageContentItem(TypedDict, total=False):
    type: Required[Literal["image"]]

    data: str

    url: URL


class TextContentItem(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


InterleavedContentItem: TypeAlias = Union[ImageContentItem, TextContentItem]

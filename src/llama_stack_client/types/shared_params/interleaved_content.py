# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .interleaved_content_item import InterleavedContentItem

__all__ = ["InterleavedContent", "ImageContentItem", "TextContentItem"]


class ImageContentItem(TypedDict, total=False):
    data: Required[str]

    type: Required[Literal["image"]]


class TextContentItem(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


InterleavedContent: TypeAlias = Union[str, ImageContentItem, TextContentItem, Iterable[InterleavedContentItem]]

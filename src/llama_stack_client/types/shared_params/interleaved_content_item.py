# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .url import URL

__all__ = ["InterleavedContentItem", "Image", "ImageImage", "Text"]


class ImageImage(TypedDict, total=False):
    data: str

    url: URL


class Image(TypedDict, total=False):
    image: Required[ImageImage]

    type: Required[Literal["image"]]


class Text(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


InterleavedContentItem: TypeAlias = Union[Image, Text]

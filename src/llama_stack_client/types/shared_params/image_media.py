# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["ImageMedia", "Image", "ImageThisClassRepresentsAnImageObjectToCreate"]


class ImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


Image: TypeAlias = Union[ImageThisClassRepresentsAnImageObjectToCreate, str]


class ImageMedia(TypedDict, total=False):
    image: Required[Image]

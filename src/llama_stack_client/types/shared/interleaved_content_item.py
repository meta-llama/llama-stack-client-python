# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .url import URL
from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["InterleavedContentItem", "ImageContentItem", "ImageContentItemImage", "TextContentItem"]


class ImageContentItemImage(BaseModel):
    data: Optional[str] = None

    url: Optional[URL] = None


class ImageContentItem(BaseModel):
    image: ImageContentItemImage

    type: Literal["image"]


class TextContentItem(BaseModel):
    text: str

    type: Literal["text"]


InterleavedContentItem: TypeAlias = Annotated[
    Union[ImageContentItem, TextContentItem], PropertyInfo(discriminator="type")
]

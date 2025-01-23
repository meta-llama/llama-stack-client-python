# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .url import URL
from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["InterleavedContentItem", "Image", "ImageImage", "Text"]


class ImageImage(BaseModel):
    data: Optional[str] = None

    url: Optional[URL] = None


class Image(BaseModel):
    image: ImageImage

    type: Literal["image"]


class Text(BaseModel):
    text: str

    type: Literal["text"]


InterleavedContentItem: TypeAlias = Annotated[Union[Image, Text], PropertyInfo(discriminator="type")]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ImageMedia", "Image", "ImageThisClassRepresentsAnImageObjectToCreate"]


class ImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


Image: TypeAlias = Union[ImageThisClassRepresentsAnImageObjectToCreate, str]


class ImageMedia(BaseModel):
    image: Image

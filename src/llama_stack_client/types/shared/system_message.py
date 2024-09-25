# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "SystemMessage",
    "Content",
    "ContentImageMedia",
    "ContentImageMediaImage",
    "ContentImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "ContentUnionMember2",
    "ContentUnionMember2ImageMedia",
    "ContentUnionMember2ImageMediaImage",
    "ContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
]


class ContentImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


ContentImageMediaImage: TypeAlias = Union[ContentImageMediaImageThisClassRepresentsAnImageObjectToCreate, str]


class ContentImageMedia(BaseModel):
    image: ContentImageMediaImage


class ContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


ContentUnionMember2ImageMediaImage: TypeAlias = Union[
    ContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class ContentUnionMember2ImageMedia(BaseModel):
    image: ContentUnionMember2ImageMediaImage


ContentUnionMember2: TypeAlias = Union[str, ContentUnionMember2ImageMedia]

Content: TypeAlias = Union[str, ContentImageMedia, List[ContentUnionMember2]]


class SystemMessage(BaseModel):
    content: Content

    role: Literal["system"]

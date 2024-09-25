# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "UserMessage",
    "Content",
    "ContentImageMedia",
    "ContentImageMediaImage",
    "ContentImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "ContentUnionMember2",
    "ContentUnionMember2ImageMedia",
    "ContentUnionMember2ImageMediaImage",
    "ContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "Context",
    "ContextImageMedia",
    "ContextImageMediaImage",
    "ContextImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "ContextUnionMember2",
    "ContextUnionMember2ImageMedia",
    "ContextUnionMember2ImageMediaImage",
    "ContextUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
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


class ContextImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


ContextImageMediaImage: TypeAlias = Union[ContextImageMediaImageThisClassRepresentsAnImageObjectToCreate, str]


class ContextImageMedia(BaseModel):
    image: ContextImageMediaImage


class ContextUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


ContextUnionMember2ImageMediaImage: TypeAlias = Union[
    ContextUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class ContextUnionMember2ImageMedia(BaseModel):
    image: ContextUnionMember2ImageMediaImage


ContextUnionMember2: TypeAlias = Union[str, ContextUnionMember2ImageMedia]

Context: TypeAlias = Union[str, ContextImageMedia, List[ContextUnionMember2]]


class UserMessage(BaseModel):
    content: Content

    role: Literal["user"]

    context: Optional[Context] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

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


class ContentImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


ContentImageMediaImage: TypeAlias = Union[ContentImageMediaImageThisClassRepresentsAnImageObjectToCreate, str]


class ContentImageMedia(TypedDict, total=False):
    image: Required[ContentImageMediaImage]


class ContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


ContentUnionMember2ImageMediaImage: TypeAlias = Union[
    ContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class ContentUnionMember2ImageMedia(TypedDict, total=False):
    image: Required[ContentUnionMember2ImageMediaImage]


ContentUnionMember2: TypeAlias = Union[str, ContentUnionMember2ImageMedia]

Content: TypeAlias = Union[str, ContentImageMedia, List[ContentUnionMember2]]


class ContextImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


ContextImageMediaImage: TypeAlias = Union[ContextImageMediaImageThisClassRepresentsAnImageObjectToCreate, str]


class ContextImageMedia(TypedDict, total=False):
    image: Required[ContextImageMediaImage]


class ContextUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


ContextUnionMember2ImageMediaImage: TypeAlias = Union[
    ContextUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class ContextUnionMember2ImageMedia(TypedDict, total=False):
    image: Required[ContextUnionMember2ImageMediaImage]


ContextUnionMember2: TypeAlias = Union[str, ContextUnionMember2ImageMedia]

Context: TypeAlias = Union[str, ContextImageMedia, List[ContextUnionMember2]]


class UserMessage(TypedDict, total=False):
    content: Required[Content]

    role: Required[Literal["user"]]

    context: Context

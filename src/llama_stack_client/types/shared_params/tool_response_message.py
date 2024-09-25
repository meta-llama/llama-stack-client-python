# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ToolResponseMessage",
    "Content",
    "ContentImageMedia",
    "ContentImageMediaImage",
    "ContentImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "ContentUnionMember2",
    "ContentUnionMember2ImageMedia",
    "ContentUnionMember2ImageMediaImage",
    "ContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
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


class ToolResponseMessage(TypedDict, total=False):
    call_id: Required[str]

    content: Required[Content]

    role: Required[Literal["ipython"]]

    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

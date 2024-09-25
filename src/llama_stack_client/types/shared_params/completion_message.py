# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .tool_call import ToolCall

__all__ = [
    "CompletionMessage",
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


class CompletionMessage(TypedDict, total=False):
    content: Required[Content]

    role: Required[Literal["assistant"]]

    stop_reason: Required[Literal["end_of_turn", "end_of_message", "out_of_tokens"]]

    tool_calls: Required[Iterable[ToolCall]]

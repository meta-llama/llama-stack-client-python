# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..shared_params.url import URL
from ..shared_params.user_message import UserMessage
from ..shared_params.tool_response_message import ToolResponseMessage
from ..shared_params.interleaved_content_item import InterleavedContentItem

__all__ = [
    "TurnCreateParamsBase",
    "Message",
    "Document",
    "DocumentContent",
    "DocumentContentImageContentItem",
    "DocumentContentImageContentItemImage",
    "DocumentContentTextContentItem",
    "Toolgroup",
    "ToolgroupUnionMember1",
    "TurnCreateParamsNonStreaming",
    "TurnCreateParamsStreaming",
]


class TurnCreateParamsBase(TypedDict, total=False):
    agent_id: Required[str]

    messages: Required[Iterable[Message]]

    documents: Iterable[Document]

    toolgroups: List[Toolgroup]


Message: TypeAlias = Union[UserMessage, ToolResponseMessage]


class DocumentContentImageContentItemImage(TypedDict, total=False):
    data: str

    url: URL


class DocumentContentImageContentItem(TypedDict, total=False):
    image: Required[DocumentContentImageContentItemImage]

    type: Required[Literal["image"]]


class DocumentContentTextContentItem(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


DocumentContent: TypeAlias = Union[
    str, DocumentContentImageContentItem, DocumentContentTextContentItem, Iterable[InterleavedContentItem], URL
]


class Document(TypedDict, total=False):
    content: Required[DocumentContent]

    mime_type: Required[str]


class ToolgroupUnionMember1(TypedDict, total=False):
    args: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    name: Required[str]


Toolgroup: TypeAlias = Union[str, ToolgroupUnionMember1]


class TurnCreateParamsNonStreaming(TurnCreateParamsBase, total=False):
    stream: Literal[False]


class TurnCreateParamsStreaming(TurnCreateParamsBase):
    stream: Required[Literal[True]]


TurnCreateParams = Union[TurnCreateParamsNonStreaming, TurnCreateParamsStreaming]

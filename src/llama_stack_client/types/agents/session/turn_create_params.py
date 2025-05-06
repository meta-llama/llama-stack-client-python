# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...url_param import URLParam
from .agent_tool_param import AgentToolParam
from .user_message_param import UserMessageParam
from ...tool_config_param import ToolConfigParam
from .tool_response_message_param import ToolResponseMessageParam
from ...interleaved_content_item_param import InterleavedContentItemParam

__all__ = [
    "TurnCreateParams",
    "Message",
    "Document",
    "DocumentContent",
    "DocumentContentImageContentItem",
    "DocumentContentImageContentItemImage",
    "DocumentContentTextContentItem",
]


class TurnCreateParams(TypedDict, total=False):
    agent_id: Required[str]

    messages: Required[Iterable[Message]]
    """List of messages to start the turn with."""

    documents: Iterable[Document]
    """(Optional) List of documents to create the turn with."""

    stream: bool
    """(Optional) If True, generate an SSE event stream of the response.

    Defaults to False.
    """

    tool_config: ToolConfigParam
    """
    (Optional) The tool configuration to create the turn with, will be used to
    override the agent's tool_config.
    """

    toolgroups: List[AgentToolParam]
    """
    (Optional) List of toolgroups to create the turn with, will be used in addition
    to the agent's config toolgroups for the request.
    """


Message: TypeAlias = Union[UserMessageParam, ToolResponseMessageParam]


class DocumentContentImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: URLParam
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class DocumentContentImageContentItem(TypedDict, total=False):
    image: Required[DocumentContentImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class DocumentContentTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


DocumentContent: TypeAlias = Union[
    str,
    DocumentContentImageContentItem,
    DocumentContentTextContentItem,
    Iterable[InterleavedContentItemParam],
    URLParam,
]


class Document(TypedDict, total=False):
    content: Required[DocumentContent]
    """The content of the document."""

    mime_type: Required[str]
    """The MIME type of the document."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .chat_completion_tool_call_param import ChatCompletionToolCallParam
from .chat_completion_content_part_param import ChatCompletionContentPartParam

__all__ = [
    "MessageParamParam",
    "OpenAIUserMessageParam",
    "OpenAISystemMessageParam",
    "OpenAIAssistantMessageParam",
    "OpenAIToolMessageParam",
    "OpenAIDeveloperMessageParam",
]


class OpenAIUserMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[ChatCompletionContentPartParam]]]
    """The content of the message, which can include text and other media"""

    role: Required[Literal["user"]]
    """Must be "user" to identify this as a user message"""

    name: str
    """(Optional) The name of the user message participant."""


class OpenAISystemMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[ChatCompletionContentPartParam]]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Required[Literal["system"]]
    """Must be "system" to identify this as a system message"""

    name: str
    """(Optional) The name of the system message participant."""


class OpenAIAssistantMessageParam(TypedDict, total=False):
    role: Required[Literal["assistant"]]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, Iterable[ChatCompletionContentPartParam]]
    """The content of the model's response"""

    name: str
    """(Optional) The name of the assistant message participant."""

    tool_calls: Iterable[ChatCompletionToolCallParam]
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class OpenAIToolMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[ChatCompletionContentPartParam]]]
    """The response content from the tool"""

    role: Required[Literal["tool"]]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: Required[str]
    """Unique identifier for the tool call this response is for"""


class OpenAIDeveloperMessageParam(TypedDict, total=False):
    content: Required[Union[str, Iterable[ChatCompletionContentPartParam]]]
    """The content of the developer message"""

    role: Required[Literal["developer"]]
    """Must be "developer" to identify this as a developer message"""

    name: str
    """(Optional) The name of the developer message participant."""


MessageParamParam: TypeAlias = Union[
    OpenAIUserMessageParam,
    OpenAISystemMessageParam,
    OpenAIAssistantMessageParam,
    OpenAIToolMessageParam,
    OpenAIDeveloperMessageParam,
]

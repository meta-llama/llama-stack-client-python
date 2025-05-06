# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel
from .chat_completion_tool_call import ChatCompletionToolCall
from .chat_completion_content_part import ChatCompletionContentPart

__all__ = [
    "MessageParam",
    "OpenAIUserMessageParam",
    "OpenAISystemMessageParam",
    "OpenAIAssistantMessageParam",
    "OpenAIToolMessageParam",
    "OpenAIDeveloperMessageParam",
]


class OpenAIUserMessageParam(BaseModel):
    content: Union[str, List[ChatCompletionContentPart]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class OpenAISystemMessageParam(BaseModel):
    content: Union[str, List[ChatCompletionContentPart]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class OpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[ChatCompletionContentPart], None] = None
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[ChatCompletionToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class OpenAIToolMessageParam(BaseModel):
    content: Union[str, List[ChatCompletionContentPart]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class OpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[ChatCompletionContentPart]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


MessageParam: TypeAlias = Annotated[
    Union[
        OpenAIUserMessageParam,
        OpenAISystemMessageParam,
        OpenAIAssistantMessageParam,
        OpenAIToolMessageParam,
        OpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]

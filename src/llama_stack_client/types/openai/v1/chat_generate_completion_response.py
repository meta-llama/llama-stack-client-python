# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from .message_param import MessageParam
from ..choice_logprobs import ChoiceLogprobs
from .chat_completion_tool_call import ChatCompletionToolCall

__all__ = [
    "ChatGenerateCompletionResponse",
    "OpenAIChatCompletion",
    "OpenAIChatCompletionChoice",
    "OpenAIChatCompletionChunk",
    "OpenAIChatCompletionChunkChoice",
    "OpenAIChatCompletionChunkChoiceDelta",
]


class OpenAIChatCompletionChoice(BaseModel):
    finish_reason: str
    """The reason the model stopped generating"""

    index: int
    """The index of the choice"""

    message: MessageParam
    """The message from the model"""

    logprobs: Optional[ChoiceLogprobs] = None
    """(Optional) The log probabilities for the tokens in the message"""


class OpenAIChatCompletion(BaseModel):
    id: str
    """The ID of the chat completion"""

    choices: List[OpenAIChatCompletionChoice]
    """List of choices"""

    created: int
    """The Unix timestamp in seconds when the chat completion was created"""

    model: str
    """The model that was used to generate the chat completion"""

    object: Literal["chat.completion"]
    """The object type, which will be "chat.completion" """


class OpenAIChatCompletionChunkChoiceDelta(BaseModel):
    content: Optional[str] = None
    """(Optional) The content of the delta"""

    refusal: Optional[str] = None
    """(Optional) The refusal of the delta"""

    role: Optional[str] = None
    """(Optional) The role of the delta"""

    tool_calls: Optional[List[ChatCompletionToolCall]] = None
    """(Optional) The tool calls of the delta"""


class OpenAIChatCompletionChunkChoice(BaseModel):
    delta: OpenAIChatCompletionChunkChoiceDelta
    """The delta from the chunk"""

    finish_reason: str
    """The reason the model stopped generating"""

    index: int
    """The index of the choice"""

    logprobs: Optional[ChoiceLogprobs] = None
    """(Optional) The log probabilities for the tokens in the message"""


class OpenAIChatCompletionChunk(BaseModel):
    id: str
    """The ID of the chat completion"""

    choices: List[OpenAIChatCompletionChunkChoice]
    """List of choices"""

    created: int
    """The Unix timestamp in seconds when the chat completion was created"""

    model: str
    """The model that was used to generate the chat completion"""

    object: Literal["chat.completion.chunk"]
    """The object type, which will be "chat.completion.chunk" """


ChatGenerateCompletionResponse: TypeAlias = Union[OpenAIChatCompletion, OpenAIChatCompletionChunk]

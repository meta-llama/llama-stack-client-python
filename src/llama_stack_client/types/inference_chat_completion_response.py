# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .token_log_probs import TokenLogProbs
from .shared.tool_call import ToolCall
from .shared.content_delta import ContentDelta
from .shared.interleaved_content import InterleavedContent

__all__ = [
    "InferenceChatCompletionResponse",
    "ChatCompletionResponse",
    "ChatCompletionResponseCompletionMessage",
    "ChatCompletionResponseStreamChunk",
    "ChatCompletionResponseStreamChunkEvent",
]


class ChatCompletionResponseCompletionMessage(BaseModel):
    content: InterleavedContent

    role: Literal["assistant"]

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]

    tool_calls: List[ToolCall]


class ChatCompletionResponse(BaseModel):
    completion_message: ChatCompletionResponseCompletionMessage

    logprobs: Optional[List[TokenLogProbs]] = None


class ChatCompletionResponseStreamChunkEvent(BaseModel):
    delta: ContentDelta

    event_type: Literal["start", "complete", "progress"]

    logprobs: Optional[List[TokenLogProbs]] = None

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None


class ChatCompletionResponseStreamChunk(BaseModel):
    event: ChatCompletionResponseStreamChunkEvent


InferenceChatCompletionResponse: TypeAlias = Union[ChatCompletionResponse, ChatCompletionResponseStreamChunk]

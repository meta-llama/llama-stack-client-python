# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.tool_call import ToolCall
from .shared.completion_message import CompletionMessage

__all__ = [
    "InferenceChatCompletionResponse",
    "ChatCompletionResponse",
    "ChatCompletionResponseLogprob",
    "ChatCompletionResponseStreamChunk",
    "ChatCompletionResponseStreamChunkEvent",
    "ChatCompletionResponseStreamChunkEventDelta",
    "ChatCompletionResponseStreamChunkEventDeltaToolCallDelta",
    "ChatCompletionResponseStreamChunkEventDeltaToolCallDeltaContent",
    "ChatCompletionResponseStreamChunkEventLogprob",
]


class ChatCompletionResponseLogprob(BaseModel):
    logprobs_by_token: Dict[str, float]


class ChatCompletionResponse(BaseModel):
    completion_message: CompletionMessage

    logprobs: Optional[List[ChatCompletionResponseLogprob]] = None


ChatCompletionResponseStreamChunkEventDeltaToolCallDeltaContent: TypeAlias = Union[str, ToolCall]


class ChatCompletionResponseStreamChunkEventDeltaToolCallDelta(BaseModel):
    content: ChatCompletionResponseStreamChunkEventDeltaToolCallDeltaContent

    parse_status: Literal["started", "in_progress", "failure", "success"]


ChatCompletionResponseStreamChunkEventDelta: TypeAlias = Union[
    str, ChatCompletionResponseStreamChunkEventDeltaToolCallDelta
]


class ChatCompletionResponseStreamChunkEventLogprob(BaseModel):
    logprobs_by_token: Dict[str, float]


class ChatCompletionResponseStreamChunkEvent(BaseModel):
    delta: ChatCompletionResponseStreamChunkEventDelta

    event_type: Literal["start", "complete", "progress"]

    logprobs: Optional[List[ChatCompletionResponseStreamChunkEventLogprob]] = None

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None


class ChatCompletionResponseStreamChunk(BaseModel):
    event: ChatCompletionResponseStreamChunkEvent


InferenceChatCompletionResponse: TypeAlias = Union[ChatCompletionResponse, ChatCompletionResponseStreamChunk]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .token_log_probs import TokenLogProbs
from .shared.completion_message import CompletionMessage
from .chat_completion_stream_chunk import ChatCompletionStreamChunk

__all__ = ["InferenceChatCompletionResponse", "ChatCompletionResponse"]


class ChatCompletionResponse(BaseModel):
    completion_message: CompletionMessage

    logprobs: Optional[List[TokenLogProbs]] = None


InferenceChatCompletionResponse: TypeAlias = Union[ChatCompletionResponse, ChatCompletionStreamChunk]

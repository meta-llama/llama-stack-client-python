# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .shared.tool_call import ToolCall
from .shared.interleaved_content import InterleavedContent

__all__ = ["BatchInferenceChatCompletionResponse", "CompletionMessageBatch"]


class CompletionMessageBatch(BaseModel):
    content: InterleavedContent

    role: Literal["assistant"]

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]

    tool_calls: List[ToolCall]


class BatchInferenceChatCompletionResponse(BaseModel):
    completion_message_batch: List[CompletionMessageBatch]

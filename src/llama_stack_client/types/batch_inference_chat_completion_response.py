# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.completion_message import CompletionMessage

__all__ = ["BatchInferenceChatCompletionResponse"]


class BatchInferenceChatCompletionResponse(BaseModel):
    completion_message_batch: List[CompletionMessage]

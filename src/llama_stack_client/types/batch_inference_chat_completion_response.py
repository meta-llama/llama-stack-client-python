# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.chat_completion_response import ChatCompletionResponse

__all__ = ["BatchInferenceChatCompletionResponse"]


class BatchInferenceChatCompletionResponse(BaseModel):
    batch: List[ChatCompletionResponse]

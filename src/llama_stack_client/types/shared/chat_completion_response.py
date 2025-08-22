# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .metric import Metric
from ..._models import BaseModel
from .completion_message import CompletionMessage
from .shared_token_log_probs import SharedTokenLogProbs

__all__ = ["ChatCompletionResponse"]


class ChatCompletionResponse(BaseModel):
    completion_message: CompletionMessage
    """The complete response message"""

    logprobs: Optional[List[SharedTokenLogProbs]] = None
    """Optional log probabilities for generated tokens"""

    metrics: Optional[List[Metric]] = None
    """(Optional) List of metrics associated with the API response"""

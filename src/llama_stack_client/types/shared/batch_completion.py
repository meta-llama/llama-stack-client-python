# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .shared_token_log_probs import SharedTokenLogProbs

__all__ = ["BatchCompletion", "Batch", "BatchMetric"]


class BatchMetric(BaseModel):
    metric: str
    """The name of the metric"""

    value: float
    """The numeric value of the metric"""

    unit: Optional[str] = None
    """(Optional) The unit of measurement for the metric value"""


class Batch(BaseModel):
    content: str
    """The generated completion text"""

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]
    """Reason why generation stopped"""

    logprobs: Optional[List[SharedTokenLogProbs]] = None
    """Optional log probabilities for generated tokens"""

    metrics: Optional[List[BatchMetric]] = None
    """(Optional) List of metrics associated with the API response"""


class BatchCompletion(BaseModel):
    batch: List[Batch]
    """List of completion responses, one for each input in the batch"""

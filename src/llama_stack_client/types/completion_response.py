# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .token_log_probs import TokenLogProbs

__all__ = ["CompletionResponse", "Metric"]


class Metric(BaseModel):
    metric: str

    value: float

    unit: Optional[str] = None


class CompletionResponse(BaseModel):
    content: str
    """The generated completion text"""

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]
    """Reason why generation stopped"""

    logprobs: Optional[List[TokenLogProbs]] = None
    """Optional log probabilities for generated tokens"""

    metrics: Optional[List[Metric]] = None

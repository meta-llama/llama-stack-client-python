# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .token_log_probs import TokenLogProbs

__all__ = ["CompletionResponse", "Metric"]


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class CompletionResponse(BaseModel):
    content: str
    """The generated completion text"""

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]
    """Reason why generation stopped"""

    logprobs: Optional[List[TokenLogProbs]] = None
    """Optional log probabilities for generated tokens"""

    metrics: Optional[List[Metric]] = None

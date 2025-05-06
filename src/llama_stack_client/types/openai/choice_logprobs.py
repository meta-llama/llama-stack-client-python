# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .token_log_prob import TokenLogProb

__all__ = ["ChoiceLogprobs"]


class ChoiceLogprobs(BaseModel):
    content: Optional[List[TokenLogProb]] = None
    """(Optional) The log probabilities for the tokens in the message"""

    refusal: Optional[List[TokenLogProb]] = None
    """(Optional) The log probabilities for the tokens in the message"""

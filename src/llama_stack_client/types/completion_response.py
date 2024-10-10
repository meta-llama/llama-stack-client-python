# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .shared.completion_message import CompletionMessage

__all__ = ["CompletionResponse", "Logprob"]


class Logprob(BaseModel):
    logprobs_by_token: Dict[str, float]


class CompletionResponse(BaseModel):
    completion_message: CompletionMessage

    logprobs: Optional[List[Logprob]] = None

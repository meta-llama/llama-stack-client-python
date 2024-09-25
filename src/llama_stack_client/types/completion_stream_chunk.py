# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .token_log_probs import TokenLogProbs

__all__ = ["CompletionStreamChunk"]


class CompletionStreamChunk(BaseModel):
    delta: str

    logprobs: Optional[List[TokenLogProbs]] = None

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None

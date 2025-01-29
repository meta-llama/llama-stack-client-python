# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .token_log_probs import TokenLogProbs
from .completion_response import CompletionResponse

__all__ = ["InferenceCompletionResponse", "CompletionResponseStreamChunk"]


class CompletionResponseStreamChunk(BaseModel):
    delta: str
    """New content generated since last chunk. This can be one or more tokens."""

    logprobs: Optional[List[TokenLogProbs]] = None
    """Optional log probabilities for generated tokens"""

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None
    """Optional reason why generation stopped, if complete"""


InferenceCompletionResponse: TypeAlias = Union[CompletionResponse, CompletionResponseStreamChunk]

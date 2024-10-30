# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .token_log_probs import TokenLogProbs
from .completion_response import CompletionResponse

__all__ = ["InferenceCompletionResponse", "CompletionResponseStreamChunk"]


class CompletionResponseStreamChunk(BaseModel):
    delta: str

    logprobs: Optional[List[TokenLogProbs]] = None

    stop_reason: Optional[Literal["end_of_turn", "end_of_message", "out_of_tokens"]] = None


InferenceCompletionResponse: TypeAlias = Union[CompletionResponse, CompletionResponseStreamChunk]

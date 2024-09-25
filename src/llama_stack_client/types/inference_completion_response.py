# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .token_log_probs import TokenLogProbs
from .completion_stream_chunk import CompletionStreamChunk
from .shared.completion_message import CompletionMessage

__all__ = ["InferenceCompletionResponse", "CompletionResponse"]


class CompletionResponse(BaseModel):
    completion_message: CompletionMessage

    logprobs: Optional[List[TokenLogProbs]] = None


InferenceCompletionResponse: TypeAlias = Union[CompletionResponse, CompletionStreamChunk]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

from .shared_params.response_format import ResponseFormat
from .shared_params.sampling_params import SamplingParams
from .shared_params.interleaved_content import InterleavedContent

__all__ = [
    "InferenceCompletionParamsBase",
    "Logprobs",
    "InferenceCompletionParamsNonStreaming",
    "InferenceCompletionParamsStreaming",
]


class InferenceCompletionParamsBase(TypedDict, total=False):
    content: Required[InterleavedContent]
    """The content to generate a completion for."""

    model_id: Required[str]
    """The identifier of the model to use.

    The model must be registered with Llama Stack and available via the /models
    endpoint.
    """

    logprobs: Logprobs
    """
    (Optional) If specified, log probabilities for each token position will be
    returned.
    """

    response_format: ResponseFormat
    """(Optional) Grammar specification for guided (structured) decoding."""

    sampling_params: SamplingParams
    """(Optional) Parameters to control the sampling strategy."""


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""


class InferenceCompletionParamsNonStreaming(InferenceCompletionParamsBase, total=False):
    stream: Literal[False]
    """(Optional) If True, generate an SSE event stream of the response.

    Defaults to False.
    """


class InferenceCompletionParamsStreaming(InferenceCompletionParamsBase):
    stream: Required[Literal[True]]
    """(Optional) If True, generate an SSE event stream of the response.

    Defaults to False.
    """


InferenceCompletionParams = Union[InferenceCompletionParamsNonStreaming, InferenceCompletionParamsStreaming]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .response_format_param import ResponseFormatParam
from .sampling_params_param import SamplingParamsParam
from .interleaved_content_param import InterleavedContentParam

__all__ = ["InferenceCompletionParams", "Logprobs"]


class InferenceCompletionParams(TypedDict, total=False):
    content: Required[InterleavedContentParam]
    """The content to generate a completion for"""

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

    response_format: ResponseFormatParam
    """(Optional) Grammar specification for guided (structured) decoding"""

    sampling_params: SamplingParamsParam
    """(Optional) Parameters to control the sampling strategy"""

    stream: bool
    """(Optional) If True, generate an SSE event stream of the response.

    Defaults to False.
    """


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""

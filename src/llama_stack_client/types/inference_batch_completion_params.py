# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .response_format_param import ResponseFormatParam
from .sampling_params_param import SamplingParamsParam
from .interleaved_content_param import InterleavedContentParam

__all__ = ["InferenceBatchCompletionParams", "Logprobs"]


class InferenceBatchCompletionParams(TypedDict, total=False):
    content_batch: Required[List[InterleavedContentParam]]

    model_id: Required[str]

    logprobs: Logprobs

    response_format: ResponseFormatParam
    """Configuration for JSON schema-guided response generation."""

    sampling_params: SamplingParamsParam
    """Sampling parameters."""


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""

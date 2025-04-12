# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .shared_params.response_format import ResponseFormat
from .shared_params.sampling_params import SamplingParams
from .shared_params.interleaved_content import InterleavedContent

__all__ = ["InferenceBatchCompletionParams", "Logprobs"]


class InferenceBatchCompletionParams(TypedDict, total=False):
    content_batch: Required[List[InterleavedContent]]

    model_id: Required[str]

    logprobs: Logprobs

    response_format: ResponseFormat
    """Configuration for JSON schema-guided response generation."""

    sampling_params: SamplingParams
    """Sampling parameters."""


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""

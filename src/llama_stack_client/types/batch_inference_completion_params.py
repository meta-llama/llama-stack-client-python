# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.sampling_params import SamplingParams
from .shared_params.interleaved_content import InterleavedContent

__all__ = ["BatchInferenceCompletionParams", "Logprobs"]


class BatchInferenceCompletionParams(TypedDict, total=False):
    content_batch: Required[List[InterleavedContent]]

    model: Required[str]

    logprobs: Logprobs

    sampling_params: SamplingParams

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class Logprobs(TypedDict, total=False):
    top_k: int

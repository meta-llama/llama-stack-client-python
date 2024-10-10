# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.image_media import ImageMedia
from .shared_params.sampling_params import SamplingParams

__all__ = ["BatchInferenceCompletionParams", "ContentBatch", "ContentBatchUnionMember2", "Logprobs"]


class BatchInferenceCompletionParams(TypedDict, total=False):
    content_batch: Required[List[ContentBatch]]

    model: Required[str]

    logprobs: Logprobs

    sampling_params: SamplingParams

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


ContentBatchUnionMember2: TypeAlias = Union[str, ImageMedia]

ContentBatch: TypeAlias = Union[str, ImageMedia, List[ContentBatchUnionMember2]]


class Logprobs(TypedDict, total=False):
    top_k: int

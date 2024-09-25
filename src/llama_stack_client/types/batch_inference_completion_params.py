# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.sampling_params import SamplingParams

__all__ = [
    "BatchInferenceCompletionParams",
    "ContentBatch",
    "ContentBatchImageMedia",
    "ContentBatchImageMediaImage",
    "ContentBatchImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "ContentBatchUnionMember2",
    "ContentBatchUnionMember2ImageMedia",
    "ContentBatchUnionMember2ImageMediaImage",
    "ContentBatchUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "Logprobs",
]


class BatchInferenceCompletionParams(TypedDict, total=False):
    content_batch: Required[List[ContentBatch]]

    model: Required[str]

    logprobs: Logprobs

    sampling_params: SamplingParams

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class ContentBatchImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


ContentBatchImageMediaImage: TypeAlias = Union[ContentBatchImageMediaImageThisClassRepresentsAnImageObjectToCreate, str]


class ContentBatchImageMedia(TypedDict, total=False):
    image: Required[ContentBatchImageMediaImage]


class ContentBatchUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


ContentBatchUnionMember2ImageMediaImage: TypeAlias = Union[
    ContentBatchUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class ContentBatchUnionMember2ImageMedia(TypedDict, total=False):
    image: Required[ContentBatchUnionMember2ImageMediaImage]


ContentBatchUnionMember2: TypeAlias = Union[str, ContentBatchUnionMember2ImageMedia]

ContentBatch: TypeAlias = Union[str, ContentBatchImageMedia, List[ContentBatchUnionMember2]]


class Logprobs(TypedDict, total=False):
    top_k: int

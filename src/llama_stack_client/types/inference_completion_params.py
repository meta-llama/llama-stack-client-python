# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.image_media import ImageMedia
from .shared_params.sampling_params import SamplingParams

__all__ = [
    "InferenceCompletionParamsBase",
    "Content",
    "ContentImageMediaArray",
    "Logprobs",
    "ResponseFormat",
    "ResponseFormatJsonSchemaFormat",
    "ResponseFormatGrammarFormat",
    "InferenceCompletionParamsNonStreaming",
    "InferenceCompletionParamsStreaming",
]


class InferenceCompletionParamsBase(TypedDict, total=False):
    content: Required[Content]

    model_id: Required[str]

    logprobs: Logprobs

    response_format: ResponseFormat

    sampling_params: SamplingParams

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


ContentImageMediaArray: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentImageMediaArray]]


class Logprobs(TypedDict, total=False):
    top_k: int


class ResponseFormatJsonSchemaFormat(TypedDict, total=False):
    json_schema: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    type: Required[Literal["json_schema"]]


class ResponseFormatGrammarFormat(TypedDict, total=False):
    bnf: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    type: Required[Literal["grammar"]]


ResponseFormat: TypeAlias = Union[ResponseFormatJsonSchemaFormat, ResponseFormatGrammarFormat]


class InferenceCompletionParamsNonStreaming(InferenceCompletionParamsBase, total=False):
    stream: Literal[False]


class InferenceCompletionParamsStreaming(InferenceCompletionParamsBase):
    stream: Required[Literal[True]]


InferenceCompletionParams = Union[InferenceCompletionParamsNonStreaming, InferenceCompletionParamsStreaming]

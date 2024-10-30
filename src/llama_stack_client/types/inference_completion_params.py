# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.image_media import ImageMedia
from .shared_params.sampling_params import SamplingParams

__all__ = [
    "InferenceCompletionParams",
    "Content",
    "ContentUnionMember2",
    "Logprobs",
    "ResponseFormat",
    "ResponseFormatUnionMember0",
    "ResponseFormatUnionMember1",
]


class InferenceCompletionParams(TypedDict, total=False):
    content: Required[Content]

    model: Required[str]

    logprobs: Logprobs

    response_format: ResponseFormat

    sampling_params: SamplingParams

    stream: bool

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


ContentUnionMember2: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentUnionMember2]]


class Logprobs(TypedDict, total=False):
    top_k: int


class ResponseFormatUnionMember0(TypedDict, total=False):
    json_schema: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    type: Required[Literal["json_schema"]]


class ResponseFormatUnionMember1(TypedDict, total=False):
    bnf: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    type: Required[Literal["grammar"]]


ResponseFormat: TypeAlias = Union[ResponseFormatUnionMember0, ResponseFormatUnionMember1]

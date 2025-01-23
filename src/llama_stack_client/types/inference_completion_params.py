# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.sampling_params import SamplingParams
from .shared_params.interleaved_content import InterleavedContent

__all__ = [
    "InferenceCompletionParamsBase",
    "Logprobs",
    "ResponseFormat",
    "ResponseFormatJsonSchema",
    "ResponseFormatGrammar",
    "InferenceCompletionParamsNonStreaming",
    "InferenceCompletionParamsStreaming",
]


class InferenceCompletionParamsBase(TypedDict, total=False):
    content: Required[InterleavedContent]

    model_id: Required[str]

    logprobs: Logprobs

    response_format: ResponseFormat

    sampling_params: SamplingParams

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]


class Logprobs(TypedDict, total=False):
    top_k: int


class ResponseFormatJsonSchema(TypedDict, total=False):
    json_schema: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    type: Required[Literal["json_schema"]]


class ResponseFormatGrammar(TypedDict, total=False):
    bnf: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    type: Required[Literal["grammar"]]


ResponseFormat: TypeAlias = Union[ResponseFormatJsonSchema, ResponseFormatGrammar]


class InferenceCompletionParamsNonStreaming(InferenceCompletionParamsBase, total=False):
    stream: Literal[False]


class InferenceCompletionParamsStreaming(InferenceCompletionParamsBase):
    stream: Required[Literal[True]]


InferenceCompletionParams = Union[InferenceCompletionParamsNonStreaming, InferenceCompletionParamsStreaming]

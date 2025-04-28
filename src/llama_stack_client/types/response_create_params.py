# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ResponseCreateParamsBase",
    "InputUnionMember1",
    "InputUnionMember1ContentUnionMember1",
    "InputUnionMember1ContentUnionMember1OpenAIResponseInputMessageContentText",
    "InputUnionMember1ContentUnionMember1OpenAIResponseInputMessageContentImage",
    "Tool",
    "ResponseCreateParamsNonStreaming",
    "ResponseCreateParamsStreaming",
]


class ResponseCreateParamsBase(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputUnionMember1]]]
    """Input message(s) to create the response."""

    model: Required[str]
    """The underlying LLM used for completions."""

    previous_response_id: str
    """
    (Optional) if specified, the new response will be a continuation of the previous
    response. This can be used to easily fork-off new responses from existing
    responses.
    """

    store: bool

    tools: Iterable[Tool]


class InputUnionMember1ContentUnionMember1OpenAIResponseInputMessageContentText(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["input_text"]]


class InputUnionMember1ContentUnionMember1OpenAIResponseInputMessageContentImage(TypedDict, total=False):
    detail: Required[Literal["low", "high", "auto"]]

    type: Required[Literal["input_image"]]

    image_url: str


InputUnionMember1ContentUnionMember1: TypeAlias = Union[
    InputUnionMember1ContentUnionMember1OpenAIResponseInputMessageContentText,
    InputUnionMember1ContentUnionMember1OpenAIResponseInputMessageContentImage,
]


class InputUnionMember1(TypedDict, total=False):
    content: Required[Union[str, Iterable[InputUnionMember1ContentUnionMember1]]]

    role: Required[Literal["system", "developer", "user", "assistant"]]

    type: Literal["message"]


class Tool(TypedDict, total=False):
    type: Required[Literal["web_search", "web_search_preview_2025_03_11"]]

    search_context_size: str


class ResponseCreateParamsNonStreaming(ResponseCreateParamsBase, total=False):
    stream: Literal[False]


class ResponseCreateParamsStreaming(ResponseCreateParamsBase):
    stream: Required[Literal[True]]


ResponseCreateParams = Union[ResponseCreateParamsNonStreaming, ResponseCreateParamsStreaming]

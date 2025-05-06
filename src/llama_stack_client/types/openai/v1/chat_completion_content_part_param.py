# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ChatCompletionContentPartParam",
    "OpenAIChatCompletionContentPartTextParam",
    "OpenAIChatCompletionContentPartImageParam",
    "OpenAIChatCompletionContentPartImageParamImageURL",
]


class OpenAIChatCompletionContentPartTextParam(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


class OpenAIChatCompletionContentPartImageParamImageURL(TypedDict, total=False):
    url: Required[str]

    detail: str


class OpenAIChatCompletionContentPartImageParam(TypedDict, total=False):
    image_url: Required[OpenAIChatCompletionContentPartImageParamImageURL]

    type: Required[Literal["image_url"]]


ChatCompletionContentPartParam: TypeAlias = Union[
    OpenAIChatCompletionContentPartTextParam, OpenAIChatCompletionContentPartImageParam
]

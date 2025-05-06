# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = [
    "ChatCompletionContentPart",
    "OpenAIChatCompletionContentPartTextParam",
    "OpenAIChatCompletionContentPartImageParam",
    "OpenAIChatCompletionContentPartImageParamImageURL",
]


class OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class OpenAIChatCompletionContentPartImageParamImageURL(BaseModel):
    url: str

    detail: Optional[str] = None


class OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: OpenAIChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


ChatCompletionContentPart: TypeAlias = Annotated[
    Union[OpenAIChatCompletionContentPartTextParam, OpenAIChatCompletionContentPartImageParam],
    PropertyInfo(discriminator="type"),
]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .response_object import ResponseObject

__all__ = [
    "ResponseObjectStream",
    "OpenAIResponseObjectStreamResponseCreated",
    "OpenAIResponseObjectStreamResponseOutputTextDelta",
    "OpenAIResponseObjectStreamResponseCompleted",
]


class OpenAIResponseObjectStreamResponseCreated(BaseModel):
    response: ResponseObject

    type: Literal["response.created"]


class OpenAIResponseObjectStreamResponseOutputTextDelta(BaseModel):
    content_index: int

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.output_text.delta"]


class OpenAIResponseObjectStreamResponseCompleted(BaseModel):
    response: ResponseObject

    type: Literal["response.completed"]


ResponseObjectStream: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseCreated,
        OpenAIResponseObjectStreamResponseOutputTextDelta,
        OpenAIResponseObjectStreamResponseCompleted,
    ],
    PropertyInfo(discriminator="type"),
]

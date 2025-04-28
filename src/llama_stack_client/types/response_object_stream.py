# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .response_object import ResponseObject

__all__ = [
    "ResponseObjectStream",
    "OpenAIResponseObjectStreamResponseCreated",
    "OpenAIResponseObjectStreamResponseCompleted",
]


class OpenAIResponseObjectStreamResponseCreated(BaseModel):
    response: ResponseObject

    type: Literal["response.created"]


class OpenAIResponseObjectStreamResponseCompleted(BaseModel):
    response: ResponseObject

    type: Literal["response.completed"]


ResponseObjectStream: TypeAlias = Annotated[
    Union[OpenAIResponseObjectStreamResponseCreated, OpenAIResponseObjectStreamResponseCompleted],
    PropertyInfo(discriminator="type"),
]

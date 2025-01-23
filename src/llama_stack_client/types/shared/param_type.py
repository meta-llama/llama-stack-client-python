# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import typing
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ParamType",
    "String",
    "Number",
    "Boolean",
    "Array",
    "Object",
    "Json",
    "Union",
    "ChatCompletionInput",
    "CompletionInput",
    "AgentTurnInput",
]


class String(BaseModel):
    type: Literal["string"]


class Number(BaseModel):
    type: Literal["number"]


class Boolean(BaseModel):
    type: Literal["boolean"]


class Array(BaseModel):
    type: Literal["array"]


class Object(BaseModel):
    type: Literal["object"]


class Json(BaseModel):
    type: Literal["json"]


class Union(BaseModel):
    type: Literal["union"]


class ChatCompletionInput(BaseModel):
    type: Literal["chat_completion_input"]


class CompletionInput(BaseModel):
    type: Literal["completion_input"]


class AgentTurnInput(BaseModel):
    type: Literal["agent_turn_input"]


ParamType: TypeAlias = Annotated[
    typing.Union[
        String, Number, Boolean, Array, Object, Json, Union, ChatCompletionInput, CompletionInput, AgentTurnInput
    ],
    PropertyInfo(discriminator="type"),
]

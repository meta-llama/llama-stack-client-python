# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "ParamType",
    "StringType",
    "NumberType",
    "BooleanType",
    "ArrayType",
    "ObjectType",
    "JsonType",
    "UnionType",
    "ChatCompletionInputType",
    "CompletionInputType",
    "AgentTurnInputType",
]


class StringType(BaseModel):
    type: Literal["string"]


class NumberType(BaseModel):
    type: Literal["number"]


class BooleanType(BaseModel):
    type: Literal["boolean"]


class ArrayType(BaseModel):
    type: Literal["array"]


class ObjectType(BaseModel):
    type: Literal["object"]


class JsonType(BaseModel):
    type: Literal["json"]


class UnionType(BaseModel):
    type: Literal["union"]


class ChatCompletionInputType(BaseModel):
    type: Literal["chat_completion_input"]


class CompletionInputType(BaseModel):
    type: Literal["completion_input"]


class AgentTurnInputType(BaseModel):
    type: Literal["agent_turn_input"]


ParamType: TypeAlias = Annotated[
    Union[
        StringType,
        NumberType,
        BooleanType,
        ArrayType,
        ObjectType,
        JsonType,
        UnionType,
        ChatCompletionInputType,
        CompletionInputType,
        AgentTurnInputType,
    ],
    PropertyInfo(discriminator="type"),
]

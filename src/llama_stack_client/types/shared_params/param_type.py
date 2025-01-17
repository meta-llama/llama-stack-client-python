# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

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


class StringType(TypedDict, total=False):
    type: Required[Literal["string"]]


class NumberType(TypedDict, total=False):
    type: Required[Literal["number"]]


class BooleanType(TypedDict, total=False):
    type: Required[Literal["boolean"]]


class ArrayType(TypedDict, total=False):
    type: Required[Literal["array"]]


class ObjectType(TypedDict, total=False):
    type: Required[Literal["object"]]


class JsonType(TypedDict, total=False):
    type: Required[Literal["json"]]


class UnionType(TypedDict, total=False):
    type: Required[Literal["union"]]


class ChatCompletionInputType(TypedDict, total=False):
    type: Required[Literal["chat_completion_input"]]


class CompletionInputType(TypedDict, total=False):
    type: Required[Literal["completion_input"]]


class AgentTurnInputType(TypedDict, total=False):
    type: Required[Literal["agent_turn_input"]]


ParamType: TypeAlias = Union[
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
]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing
from typing_extensions import Literal, Required, TypeAlias, TypedDict

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


class String(TypedDict, total=False):
    type: Required[Literal["string"]]


class Number(TypedDict, total=False):
    type: Required[Literal["number"]]


class Boolean(TypedDict, total=False):
    type: Required[Literal["boolean"]]


class Array(TypedDict, total=False):
    type: Required[Literal["array"]]


class Object(TypedDict, total=False):
    type: Required[Literal["object"]]


class Json(TypedDict, total=False):
    type: Required[Literal["json"]]


class Union(TypedDict, total=False):
    type: Required[Literal["union"]]


class ChatCompletionInput(TypedDict, total=False):
    type: Required[Literal["chat_completion_input"]]


class CompletionInput(TypedDict, total=False):
    type: Required[Literal["completion_input"]]


class AgentTurnInput(TypedDict, total=False):
    type: Required[Literal["agent_turn_input"]]


ParamType: TypeAlias = typing.Union[
    String, Number, Boolean, Array, Object, Json, Union, ChatCompletionInput, CompletionInput, AgentTurnInput
]

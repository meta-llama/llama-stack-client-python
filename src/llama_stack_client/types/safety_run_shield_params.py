# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.tool_call import ToolCall
from .shared_params.user_message import UserMessage
from .shared_params.system_message import SystemMessage
from .shared_params.interleaved_content import InterleavedContent
from .shared_params.tool_response_message import ToolResponseMessage

__all__ = ["SafetyRunShieldParams", "Message", "MessageCompletionMessage"]


class SafetyRunShieldParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    params: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    shield_id: Required[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class MessageCompletionMessage(TypedDict, total=False):
    content: Required[InterleavedContent]

    role: Required[Literal["assistant"]]

    stop_reason: Required[Literal["end_of_turn", "end_of_message", "out_of_tokens"]]

    tool_calls: Required[Iterable[ToolCall]]


Message: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, MessageCompletionMessage]

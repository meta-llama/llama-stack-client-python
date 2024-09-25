# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.user_message import UserMessage
from .shared_params.system_message import SystemMessage
from .shared_params.completion_message import CompletionMessage
from .shared_params.tool_response_message import ToolResponseMessage

__all__ = ["SafetyRunShieldParams", "Message"]


class SafetyRunShieldParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    params: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    shield_type: Required[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


Message: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]

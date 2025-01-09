# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.tool_call import ToolCall
from .shared_params.user_message import UserMessage
from .shared_params.system_message import SystemMessage
from .shared_params.interleaved_content import InterleavedContent
from .shared_params.tool_response_message import ToolResponseMessage

__all__ = ["SyntheticDataGenerationGenerateParams", "Dialog", "DialogCompletionMessage"]


class SyntheticDataGenerationGenerateParams(TypedDict, total=False):
    dialogs: Required[Iterable[Dialog]]

    filtering_function: Required[Literal["none", "random", "top_k", "top_p", "top_k_top_p", "sigmoid"]]

    model: str

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]


class DialogCompletionMessage(TypedDict, total=False):
    content: Required[InterleavedContent]

    role: Required[Literal["assistant"]]

    stop_reason: Required[Literal["end_of_turn", "end_of_message", "out_of_tokens"]]

    tool_calls: Required[Iterable[ToolCall]]


Dialog: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, DialogCompletionMessage]

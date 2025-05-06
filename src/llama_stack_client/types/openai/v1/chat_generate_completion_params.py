# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .message_param_param import MessageParamParam

__all__ = [
    "ChatGenerateCompletionParams",
    "ResponseFormat",
    "ResponseFormatOpenAIResponseFormatText",
    "ResponseFormatOpenAIResponseFormatJsonSchema",
    "ResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema",
    "ResponseFormatOpenAIResponseFormatJsonObject",
]


class ChatGenerateCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[MessageParamParam]]
    """List of messages in the conversation"""

    model: Required[str]
    """The identifier of the model to use.

    The model must be registered with Llama Stack and available via the /models
    endpoint.
    """

    frequency_penalty: float
    """(Optional) The penalty for repeated tokens"""

    function_call: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """(Optional) The function call to use"""

    functions: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """(Optional) List of functions to use"""

    logit_bias: Dict[str, float]
    """(Optional) The logit bias to use"""

    logprobs: bool
    """(Optional) The log probabilities to use"""

    max_completion_tokens: int
    """(Optional) The maximum number of tokens to generate"""

    max_tokens: int
    """(Optional) The maximum number of tokens to generate"""

    n: int
    """(Optional) The number of completions to generate"""

    parallel_tool_calls: bool
    """(Optional) Whether to parallelize tool calls"""

    presence_penalty: float
    """(Optional) The penalty for repeated tokens"""

    response_format: ResponseFormat
    """(Optional) The response format to use"""

    seed: int
    """(Optional) The seed to use"""

    stop: Union[str, List[str]]
    """(Optional) The stop tokens to use"""

    stream: bool
    """(Optional) Whether to stream the response"""

    stream_options: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """(Optional) The stream options to use"""

    temperature: float
    """(Optional) The temperature to use"""

    tool_choice: Union[str, Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """(Optional) The tool choice to use"""

    tools: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """(Optional) The tools to use"""

    top_logprobs: int
    """(Optional) The top log probabilities to use"""

    top_p: float
    """(Optional) The top p to use"""

    user: str
    """(Optional) The user to use"""


class ResponseFormatOpenAIResponseFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]


class ResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema(TypedDict, total=False):
    name: Required[str]

    description: str

    schema: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    strict: bool


class ResponseFormatOpenAIResponseFormatJsonSchema(TypedDict, total=False):
    json_schema: Required[ResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema]

    type: Required[Literal["json_schema"]]


class ResponseFormatOpenAIResponseFormatJsonObject(TypedDict, total=False):
    type: Required[Literal["json_object"]]


ResponseFormat: TypeAlias = Union[
    ResponseFormatOpenAIResponseFormatText,
    ResponseFormatOpenAIResponseFormatJsonSchema,
    ResponseFormatOpenAIResponseFormatJsonObject,
]

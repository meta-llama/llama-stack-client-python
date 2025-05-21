# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .shared_params.message import Message
from .shared_params.response_format import ResponseFormat
from .shared_params.sampling_params import SamplingParams
from .shared_params.tool_param_definition import ToolParamDefinition

__all__ = [
    "InferenceChatCompletionParamsBase",
    "Logprobs",
    "ToolConfig",
    "Tool",
    "InferenceChatCompletionParamsNonStreaming",
    "InferenceChatCompletionParamsStreaming",
]


class InferenceChatCompletionParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """List of messages in the conversation."""

    model_id: Required[str]
    """The identifier of the model to use.

    The model must be registered with Llama Stack and available via the /models
    endpoint.
    """

    logprobs: Logprobs
    """
    (Optional) If specified, log probabilities for each token position will be
    returned.
    """

    response_format: ResponseFormat
    """(Optional) Grammar specification for guided (structured) decoding.

    There are two options: - `ResponseFormat.json_schema`: The grammar is a JSON
    schema. Most providers support this format. - `ResponseFormat.grammar`: The
    grammar is a BNF grammar. This format is more flexible, but not all providers
    support it.
    """

    sampling_params: SamplingParams
    """Parameters to control the sampling strategy."""

    tool_choice: Literal["auto", "required", "none"]
    """(Optional) Whether tool use is required or automatic.

    Defaults to ToolChoice.auto. .. deprecated:: Use tool_config instead.
    """

    tool_config: ToolConfig
    """(Optional) Configuration for tool use."""

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """(Optional) Instructs the model how to format tool calls.

    By default, Llama Stack will attempt to use a format that is best adapted to the
    model. - `ToolPromptFormat.json`: The tool calls are formatted as a JSON
    object. - `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
    <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
    are output as Python syntax -- a list of function calls. .. deprecated:: Use
    tool_config instead.
    """

    tools: Iterable[Tool]
    """(Optional) List of tool definitions available to the model."""


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""


class ToolConfig(TypedDict, total=False):
    system_message_behavior: Literal["append", "replace"]
    """(Optional) Config for how to override the default system prompt.

    - `SystemMessageBehavior.append`: Appends the provided system message to the
      default system prompt. - `SystemMessageBehavior.replace`: Replaces the default
      system prompt with the provided system message. The system message can include
      the string '{{function_definitions}}' to indicate where the function
      definitions should be inserted.
    """

    tool_choice: Union[Literal["auto", "required", "none"], str]
    """(Optional) Whether tool use is automatic, required, or none.

    Can also specify a tool name to use a specific tool. Defaults to
    ToolChoice.auto.
    """

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """(Optional) Instructs the model how to format tool calls.

    By default, Llama Stack will attempt to use a format that is best adapted to the
    model. - `ToolPromptFormat.json`: The tool calls are formatted as a JSON
    object. - `ToolPromptFormat.function_tag`: The tool calls are enclosed in a
    <function=function_name> tag. - `ToolPromptFormat.python_list`: The tool calls
    are output as Python syntax -- a list of function calls.
    """


class Tool(TypedDict, total=False):
    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

    description: str

    parameters: Dict[str, ToolParamDefinition]


class InferenceChatCompletionParamsNonStreaming(InferenceChatCompletionParamsBase, total=False):
    stream: Literal[False]
    """(Optional) If True, generate an SSE event stream of the response.

    Defaults to False.
    """


class InferenceChatCompletionParamsStreaming(InferenceChatCompletionParamsBase):
    stream: Required[Literal[True]]
    """(Optional) If True, generate an SSE event stream of the response.

    Defaults to False.
    """


InferenceChatCompletionParams = Union[InferenceChatCompletionParamsNonStreaming, InferenceChatCompletionParamsStreaming]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .message_param import MessageParam
from .tool_config_param import ToolConfigParam
from .response_format_param import ResponseFormatParam
from .sampling_params_param import SamplingParamsParam
from .tool_definition_param import ToolDefinitionParam

__all__ = ["InferenceChatCompletionParams", "Logprobs"]


class InferenceChatCompletionParams(TypedDict, total=False):
    messages: Required[Iterable[MessageParam]]
    """List of messages in the conversation"""

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

    response_format: ResponseFormatParam
    """(Optional) Grammar specification for guided (structured) decoding.

    There are two options: - `ResponseFormat.json_schema`: The grammar is a JSON
    schema. Most providers support this format. - `ResponseFormat.grammar`: The
    grammar is a BNF grammar. This format is more flexible, but not all providers
    support it.
    """

    sampling_params: SamplingParamsParam
    """Parameters to control the sampling strategy"""

    stream: bool
    """(Optional) If True, generate an SSE event stream of the response.

    Defaults to False.
    """

    tool_choice: Literal["auto", "required", "none"]
    """(Optional) Whether tool use is required or automatic.

    Defaults to ToolChoice.auto. .. deprecated:: Use tool_config instead.
    """

    tool_config: ToolConfigParam
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

    tools: Iterable[ToolDefinitionParam]
    """(Optional) List of tool definitions available to the model"""


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""

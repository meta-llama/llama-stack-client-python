# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from .shared_params.message import Message
from .shared_params.response_format import ResponseFormat
from .shared_params.sampling_params import SamplingParams
from .shared_params.tool_param_definition import ToolParamDefinition

__all__ = ["BatchInferenceChatCompletionParams", "Logprobs", "Tool"]


class BatchInferenceChatCompletionParams(TypedDict, total=False):
    messages_batch: Required[Iterable[Iterable[Message]]]

    model: Required[str]

    logprobs: Logprobs

    response_format: ResponseFormat

    sampling_params: SamplingParams

    tool_choice: Literal["auto", "required"]

    tool_prompt_format: Literal["json", "function_tag", "python_list"]

    tools: Iterable[Tool]


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""


class Tool(TypedDict, total=False):
    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

    description: str

    parameters: Dict[str, ToolParamDefinition]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .message_param import MessageParam
from .tool_config_param import ToolConfigParam
from .response_format_param import ResponseFormatParam
from .sampling_params_param import SamplingParamsParam
from .tool_definition_param import ToolDefinitionParam

__all__ = ["InferenceBatchChatCompletionParams", "Logprobs"]


class InferenceBatchChatCompletionParams(TypedDict, total=False):
    messages_batch: Required[Iterable[Iterable[MessageParam]]]

    model_id: Required[str]

    logprobs: Logprobs

    response_format: ResponseFormatParam
    """Configuration for JSON schema-guided response generation."""

    sampling_params: SamplingParamsParam
    """Sampling parameters."""

    tool_config: ToolConfigParam
    """Configuration for tool use."""

    tools: Iterable[ToolDefinitionParam]


class Logprobs(TypedDict, total=False):
    top_k: int
    """How many tokens (for each position) to return log probabilities for."""

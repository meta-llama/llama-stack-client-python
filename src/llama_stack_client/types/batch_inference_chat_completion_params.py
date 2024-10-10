# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.user_message import UserMessage
from .shared_params.system_message import SystemMessage
from .shared_params.sampling_params import SamplingParams
from .shared_params.completion_message import CompletionMessage
from .shared_params.tool_response_message import ToolResponseMessage

__all__ = ["BatchInferenceChatCompletionParams", "MessagesBatch", "Logprobs", "Tool", "ToolParameters"]


class BatchInferenceChatCompletionParams(TypedDict, total=False):
    messages_batch: Required[Iterable[Iterable[MessagesBatch]]]

    model: Required[str]

    logprobs: Logprobs

    sampling_params: SamplingParams

    tool_choice: Literal["auto", "required"]

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """
    `json` -- Refers to the json format for calling tools. The json format takes the
    form like { "type": "function", "function" : { "name": "function_name",
    "description": "function_description", "parameters": {...} } }

    `function_tag` -- This is an example of how you could define your own user
    defined format for making tool calls. The function_tag format looks like this,
    <function=function_name>(parameters)</function>

    The detailed prompts for each of these formats are added to llama cli
    """

    tools: Iterable[Tool]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


MessagesBatch: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]


class Logprobs(TypedDict, total=False):
    top_k: int


class ToolParameters(TypedDict, total=False):
    param_type: Required[str]

    default: Union[bool, float, str, Iterable[object], object, None]

    description: str

    required: bool


class Tool(TypedDict, total=False):
    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

    description: str

    parameters: Dict[str, ToolParameters]

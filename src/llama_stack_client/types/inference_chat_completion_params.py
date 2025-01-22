# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.message import Message
from .shared_params.sampling_params import SamplingParams
from .shared_params.tool_param_definition import ToolParamDefinition

__all__ = [
    "InferenceChatCompletionParamsBase",
    "Logprobs",
    "ResponseFormat",
    "ResponseFormatUnionMember0",
    "ResponseFormatUnionMember1",
    "Tool",
    "InferenceChatCompletionParamsNonStreaming",
    "InferenceChatCompletionParamsStreaming",
]


class InferenceChatCompletionParamsBase(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    model_id: Required[str]

    logprobs: Logprobs

    response_format: ResponseFormat

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

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]


class Logprobs(TypedDict, total=False):
    top_k: int


class ResponseFormatUnionMember0(TypedDict, total=False):
    json_schema: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    type: Required[Literal["json_schema"]]


class ResponseFormatUnionMember1(TypedDict, total=False):
    bnf: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    type: Required[Literal["grammar"]]


ResponseFormat: TypeAlias = Union[ResponseFormatUnionMember0, ResponseFormatUnionMember1]


class Tool(TypedDict, total=False):
    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

    description: str

    parameters: Dict[str, ToolParamDefinition]


class InferenceChatCompletionParamsNonStreaming(InferenceChatCompletionParamsBase, total=False):
    stream: Literal[False]


class InferenceChatCompletionParamsStreaming(InferenceChatCompletionParamsBase):
    stream: Required[Literal[True]]


InferenceChatCompletionParams = Union[InferenceChatCompletionParamsNonStreaming, InferenceChatCompletionParamsStreaming]

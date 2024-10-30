# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.sampling_params import SamplingParams
from .rest_api_execution_config_param import RestAPIExecutionConfigParam

__all__ = [
    "AgentCreateParams",
    "AgentConfig",
    "AgentConfigTool",
    "AgentConfigToolSearchToolDefinition",
    "AgentConfigToolWolframAlphaToolDefinition",
    "AgentConfigToolPhotogenToolDefinition",
    "AgentConfigToolCodeInterpreterToolDefinition",
    "AgentConfigToolFunctionCallToolDefinition",
    "AgentConfigToolFunctionCallToolDefinitionParameters",
    "AgentConfigToolMemoryToolDefinition",
    "AgentConfigToolMemoryToolDefinitionMemoryBankConfig",
    "AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember0",
    "AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember1",
    "AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember2",
    "AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember3",
    "AgentConfigToolMemoryToolDefinitionQueryGeneratorConfig",
    "AgentConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember0",
    "AgentConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember1",
    "AgentConfigToolMemoryToolDefinitionQueryGeneratorConfigType",
]


class AgentCreateParams(TypedDict, total=False):
    agent_config: Required[AgentConfig]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class AgentConfigToolSearchToolDefinition(TypedDict, total=False):
    api_key: Required[str]

    engine: Required[Literal["bing", "brave"]]

    type: Required[Literal["brave_search"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class AgentConfigToolWolframAlphaToolDefinition(TypedDict, total=False):
    api_key: Required[str]

    type: Required[Literal["wolfram_alpha"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class AgentConfigToolPhotogenToolDefinition(TypedDict, total=False):
    type: Required[Literal["photogen"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class AgentConfigToolCodeInterpreterToolDefinition(TypedDict, total=False):
    enable_inline_code_execution: Required[bool]

    type: Required[Literal["code_interpreter"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class AgentConfigToolFunctionCallToolDefinitionParameters(TypedDict, total=False):
    param_type: Required[str]

    default: Union[bool, float, str, Iterable[object], object, None]

    description: str

    required: bool


class AgentConfigToolFunctionCallToolDefinition(TypedDict, total=False):
    description: Required[str]

    function_name: Required[str]

    parameters: Required[Dict[str, AgentConfigToolFunctionCallToolDefinitionParameters]]

    type: Required[Literal["function_call"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember0(TypedDict, total=False):
    bank_id: Required[str]

    type: Required[Literal["vector"]]


class AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember1(TypedDict, total=False):
    bank_id: Required[str]

    keys: Required[List[str]]

    type: Required[Literal["keyvalue"]]


class AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember2(TypedDict, total=False):
    bank_id: Required[str]

    type: Required[Literal["keyword"]]


class AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember3(TypedDict, total=False):
    bank_id: Required[str]

    entities: Required[List[str]]

    type: Required[Literal["graph"]]


AgentConfigToolMemoryToolDefinitionMemoryBankConfig: TypeAlias = Union[
    AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember0,
    AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember1,
    AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember2,
    AgentConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember3,
]


class AgentConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember0(TypedDict, total=False):
    sep: Required[str]

    type: Required[Literal["default"]]


class AgentConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember1(TypedDict, total=False):
    model: Required[str]

    template: Required[str]

    type: Required[Literal["llm"]]


class AgentConfigToolMemoryToolDefinitionQueryGeneratorConfigType(TypedDict, total=False):
    type: Required[Literal["custom"]]


AgentConfigToolMemoryToolDefinitionQueryGeneratorConfig: TypeAlias = Union[
    AgentConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember0,
    AgentConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember1,
    AgentConfigToolMemoryToolDefinitionQueryGeneratorConfigType,
]


class AgentConfigToolMemoryToolDefinition(TypedDict, total=False):
    max_chunks: Required[int]

    max_tokens_in_context: Required[int]

    memory_bank_configs: Required[Iterable[AgentConfigToolMemoryToolDefinitionMemoryBankConfig]]

    query_generator_config: Required[AgentConfigToolMemoryToolDefinitionQueryGeneratorConfig]

    type: Required[Literal["memory"]]

    input_shields: List[str]

    output_shields: List[str]


AgentConfigTool: TypeAlias = Union[
    AgentConfigToolSearchToolDefinition,
    AgentConfigToolWolframAlphaToolDefinition,
    AgentConfigToolPhotogenToolDefinition,
    AgentConfigToolCodeInterpreterToolDefinition,
    AgentConfigToolFunctionCallToolDefinition,
    AgentConfigToolMemoryToolDefinition,
]


class AgentConfig(TypedDict, total=False):
    enable_session_persistence: Required[bool]

    instructions: Required[str]

    max_infer_iters: Required[int]

    model: Required[str]

    input_shields: List[str]

    output_shields: List[str]

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

    tools: Iterable[AgentConfigTool]

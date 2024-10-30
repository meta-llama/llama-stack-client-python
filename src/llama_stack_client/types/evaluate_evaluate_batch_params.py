# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.system_message import SystemMessage
from .shared_params.sampling_params import SamplingParams
from .rest_api_execution_config_param import RestAPIExecutionConfigParam

__all__ = [
    "EvaluateEvaluateBatchParams",
    "Candidate",
    "CandidateModelCandidate",
    "CandidateAgentCandidate",
    "CandidateAgentCandidateConfig",
    "CandidateAgentCandidateConfigTool",
    "CandidateAgentCandidateConfigToolSearchToolDefinition",
    "CandidateAgentCandidateConfigToolWolframAlphaToolDefinition",
    "CandidateAgentCandidateConfigToolPhotogenToolDefinition",
    "CandidateAgentCandidateConfigToolCodeInterpreterToolDefinition",
    "CandidateAgentCandidateConfigToolFunctionCallToolDefinition",
    "CandidateAgentCandidateConfigToolFunctionCallToolDefinitionParameters",
    "CandidateAgentCandidateConfigToolMemoryToolDefinition",
    "CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfig",
    "CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember0",
    "CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember1",
    "CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember2",
    "CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember3",
    "CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfig",
    "CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember0",
    "CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember1",
    "CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfigType",
]


class EvaluateEvaluateBatchParams(TypedDict, total=False):
    candidate: Required[Candidate]

    dataset_id: Required[str]

    scoring_functions: Required[List[str]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class CandidateModelCandidate(TypedDict, total=False):
    model: Required[str]

    sampling_params: Required[SamplingParams]

    type: Required[Literal["model"]]

    system_message: SystemMessage


class CandidateAgentCandidateConfigToolSearchToolDefinition(TypedDict, total=False):
    api_key: Required[str]

    engine: Required[Literal["bing", "brave"]]

    type: Required[Literal["brave_search"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class CandidateAgentCandidateConfigToolWolframAlphaToolDefinition(TypedDict, total=False):
    api_key: Required[str]

    type: Required[Literal["wolfram_alpha"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class CandidateAgentCandidateConfigToolPhotogenToolDefinition(TypedDict, total=False):
    type: Required[Literal["photogen"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class CandidateAgentCandidateConfigToolCodeInterpreterToolDefinition(TypedDict, total=False):
    enable_inline_code_execution: Required[bool]

    type: Required[Literal["code_interpreter"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class CandidateAgentCandidateConfigToolFunctionCallToolDefinitionParameters(TypedDict, total=False):
    param_type: Required[str]

    default: Union[bool, float, str, Iterable[object], object, None]

    description: str

    required: bool


class CandidateAgentCandidateConfigToolFunctionCallToolDefinition(TypedDict, total=False):
    description: Required[str]

    function_name: Required[str]

    parameters: Required[Dict[str, CandidateAgentCandidateConfigToolFunctionCallToolDefinitionParameters]]

    type: Required[Literal["function_call"]]

    input_shields: List[str]

    output_shields: List[str]

    remote_execution: RestAPIExecutionConfigParam


class CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember0(TypedDict, total=False):
    bank_id: Required[str]

    type: Required[Literal["vector"]]


class CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember1(TypedDict, total=False):
    bank_id: Required[str]

    keys: Required[List[str]]

    type: Required[Literal["keyvalue"]]


class CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember2(TypedDict, total=False):
    bank_id: Required[str]

    type: Required[Literal["keyword"]]


class CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember3(TypedDict, total=False):
    bank_id: Required[str]

    entities: Required[List[str]]

    type: Required[Literal["graph"]]


CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfig: TypeAlias = Union[
    CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember0,
    CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember1,
    CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember2,
    CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfigUnionMember3,
]


class CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember0(TypedDict, total=False):
    sep: Required[str]

    type: Required[Literal["default"]]


class CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember1(TypedDict, total=False):
    model: Required[str]

    template: Required[str]

    type: Required[Literal["llm"]]


class CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfigType(TypedDict, total=False):
    type: Required[Literal["custom"]]


CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfig: TypeAlias = Union[
    CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember0,
    CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfigUnionMember1,
    CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfigType,
]


class CandidateAgentCandidateConfigToolMemoryToolDefinition(TypedDict, total=False):
    max_chunks: Required[int]

    max_tokens_in_context: Required[int]

    memory_bank_configs: Required[Iterable[CandidateAgentCandidateConfigToolMemoryToolDefinitionMemoryBankConfig]]

    query_generator_config: Required[CandidateAgentCandidateConfigToolMemoryToolDefinitionQueryGeneratorConfig]

    type: Required[Literal["memory"]]

    input_shields: List[str]

    output_shields: List[str]


CandidateAgentCandidateConfigTool: TypeAlias = Union[
    CandidateAgentCandidateConfigToolSearchToolDefinition,
    CandidateAgentCandidateConfigToolWolframAlphaToolDefinition,
    CandidateAgentCandidateConfigToolPhotogenToolDefinition,
    CandidateAgentCandidateConfigToolCodeInterpreterToolDefinition,
    CandidateAgentCandidateConfigToolFunctionCallToolDefinition,
    CandidateAgentCandidateConfigToolMemoryToolDefinition,
]


class CandidateAgentCandidateConfig(TypedDict, total=False):
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

    tools: Iterable[CandidateAgentCandidateConfigTool]


class CandidateAgentCandidate(TypedDict, total=False):
    config: Required[CandidateAgentCandidateConfig]

    type: Required[Literal["agent"]]


Candidate: TypeAlias = Union[CandidateModelCandidate, CandidateAgentCandidate]

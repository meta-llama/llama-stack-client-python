# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.agent_config import AgentConfig
from .shared_params.system_message import SystemMessage
from .shared_params.sampling_params import SamplingParams

__all__ = [
    "EvalRunEvalParams",
    "TaskConfig",
    "TaskConfigBenchmark",
    "TaskConfigBenchmarkEvalCandidate",
    "TaskConfigBenchmarkEvalCandidateModel",
    "TaskConfigBenchmarkEvalCandidateAgent",
    "TaskConfigApp",
    "TaskConfigAppEvalCandidate",
    "TaskConfigAppEvalCandidateModel",
    "TaskConfigAppEvalCandidateAgent",
    "TaskConfigAppScoringParams",
    "TaskConfigAppScoringParamsLlmAsJudge",
    "TaskConfigAppScoringParamsRegexParser",
    "TaskConfigAppScoringParamsBasic",
]


class EvalRunEvalParams(TypedDict, total=False):
    task_config: Required[TaskConfig]

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]


class TaskConfigBenchmarkEvalCandidateModel(TypedDict, total=False):
    model: Required[str]

    sampling_params: Required[SamplingParams]

    type: Required[Literal["model"]]

    system_message: SystemMessage


class TaskConfigBenchmarkEvalCandidateAgent(TypedDict, total=False):
    config: Required[AgentConfig]

    type: Required[Literal["agent"]]


TaskConfigBenchmarkEvalCandidate: TypeAlias = Union[
    TaskConfigBenchmarkEvalCandidateModel, TaskConfigBenchmarkEvalCandidateAgent
]


class TaskConfigBenchmark(TypedDict, total=False):
    eval_candidate: Required[TaskConfigBenchmarkEvalCandidate]

    type: Required[Literal["benchmark"]]

    num_examples: int


class TaskConfigAppEvalCandidateModel(TypedDict, total=False):
    model: Required[str]

    sampling_params: Required[SamplingParams]

    type: Required[Literal["model"]]

    system_message: SystemMessage


class TaskConfigAppEvalCandidateAgent(TypedDict, total=False):
    config: Required[AgentConfig]

    type: Required[Literal["agent"]]


TaskConfigAppEvalCandidate: TypeAlias = Union[TaskConfigAppEvalCandidateModel, TaskConfigAppEvalCandidateAgent]


class TaskConfigAppScoringParamsLlmAsJudge(TypedDict, total=False):
    judge_model: Required[str]

    type: Required[Literal["llm_as_judge"]]

    aggregation_functions: List[Literal["average", "median", "categorical_count", "accuracy"]]

    judge_score_regexes: List[str]

    prompt_template: str


class TaskConfigAppScoringParamsRegexParser(TypedDict, total=False):
    type: Required[Literal["regex_parser"]]

    aggregation_functions: List[Literal["average", "median", "categorical_count", "accuracy"]]

    parsing_regexes: List[str]


class TaskConfigAppScoringParamsBasic(TypedDict, total=False):
    type: Required[Literal["basic"]]

    aggregation_functions: List[Literal["average", "median", "categorical_count", "accuracy"]]


TaskConfigAppScoringParams: TypeAlias = Union[
    TaskConfigAppScoringParamsLlmAsJudge, TaskConfigAppScoringParamsRegexParser, TaskConfigAppScoringParamsBasic
]


class TaskConfigApp(TypedDict, total=False):
    eval_candidate: Required[TaskConfigAppEvalCandidate]

    scoring_params: Required[Dict[str, TaskConfigAppScoringParams]]

    type: Required[Literal["app"]]

    num_examples: int


TaskConfig: TypeAlias = Union[TaskConfigBenchmark, TaskConfigApp]

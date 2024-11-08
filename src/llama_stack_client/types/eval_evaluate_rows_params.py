# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.agent_config import AgentConfig
from .shared_params.system_message import SystemMessage
from .shared_params.sampling_params import SamplingParams

__all__ = [
    "EvalEvaluateRowsParams",
    "TaskConfig",
    "TaskConfigBenchmarkEvalTaskConfig",
    "TaskConfigBenchmarkEvalTaskConfigEvalCandidate",
    "TaskConfigBenchmarkEvalTaskConfigEvalCandidateModelCandidate",
    "TaskConfigBenchmarkEvalTaskConfigEvalCandidateAgentCandidate",
    "TaskConfigAppEvalTaskConfig",
    "TaskConfigAppEvalTaskConfigEvalCandidate",
    "TaskConfigAppEvalTaskConfigEvalCandidateModelCandidate",
    "TaskConfigAppEvalTaskConfigEvalCandidateAgentCandidate",
    "TaskConfigAppEvalTaskConfigScoringParams",
    "TaskConfigAppEvalTaskConfigScoringParamsLlmAsJudgeScoringFnParams",
    "TaskConfigAppEvalTaskConfigScoringParamsRegexParserScoringFnParams",
]


class EvalEvaluateRowsParams(TypedDict, total=False):
    input_rows: Required[Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]]

    scoring_functions: Required[List[str]]

    task_config: Required[TaskConfig]

    task_id: Required[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class TaskConfigBenchmarkEvalTaskConfigEvalCandidateModelCandidate(TypedDict, total=False):
    model: Required[str]

    sampling_params: Required[SamplingParams]

    type: Required[Literal["model"]]

    system_message: SystemMessage


class TaskConfigBenchmarkEvalTaskConfigEvalCandidateAgentCandidate(TypedDict, total=False):
    config: Required[AgentConfig]

    type: Required[Literal["agent"]]


TaskConfigBenchmarkEvalTaskConfigEvalCandidate: TypeAlias = Union[
    TaskConfigBenchmarkEvalTaskConfigEvalCandidateModelCandidate,
    TaskConfigBenchmarkEvalTaskConfigEvalCandidateAgentCandidate,
]


class TaskConfigBenchmarkEvalTaskConfig(TypedDict, total=False):
    eval_candidate: Required[TaskConfigBenchmarkEvalTaskConfigEvalCandidate]

    type: Required[Literal["benchmark"]]

    num_examples: int


class TaskConfigAppEvalTaskConfigEvalCandidateModelCandidate(TypedDict, total=False):
    model: Required[str]

    sampling_params: Required[SamplingParams]

    type: Required[Literal["model"]]

    system_message: SystemMessage


class TaskConfigAppEvalTaskConfigEvalCandidateAgentCandidate(TypedDict, total=False):
    config: Required[AgentConfig]

    type: Required[Literal["agent"]]


TaskConfigAppEvalTaskConfigEvalCandidate: TypeAlias = Union[
    TaskConfigAppEvalTaskConfigEvalCandidateModelCandidate, TaskConfigAppEvalTaskConfigEvalCandidateAgentCandidate
]


class TaskConfigAppEvalTaskConfigScoringParamsLlmAsJudgeScoringFnParams(TypedDict, total=False):
    judge_model: Required[str]

    type: Required[Literal["llm_as_judge"]]

    judge_score_regexes: List[str]

    prompt_template: str


class TaskConfigAppEvalTaskConfigScoringParamsRegexParserScoringFnParams(TypedDict, total=False):
    type: Required[Literal["regex_parser"]]

    parsing_regexes: List[str]


TaskConfigAppEvalTaskConfigScoringParams: TypeAlias = Union[
    TaskConfigAppEvalTaskConfigScoringParamsLlmAsJudgeScoringFnParams,
    TaskConfigAppEvalTaskConfigScoringParamsRegexParserScoringFnParams,
]


class TaskConfigAppEvalTaskConfig(TypedDict, total=False):
    eval_candidate: Required[TaskConfigAppEvalTaskConfigEvalCandidate]

    scoring_params: Required[Dict[str, TaskConfigAppEvalTaskConfigScoringParams]]

    type: Required[Literal["app"]]

    num_examples: int


TaskConfig: TypeAlias = Union[TaskConfigBenchmarkEvalTaskConfig, TaskConfigAppEvalTaskConfig]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..agent_config_param import AgentConfigParam
from ..system_message_param import SystemMessageParam
from ..sampling_params_param import SamplingParamsParam
from ..scoring_fn_params_param import ScoringFnParamsParam

__all__ = ["BenchmarkConfigParam", "EvalCandidate", "EvalCandidateModelCandidate", "EvalCandidateAgentCandidate"]


class EvalCandidateModelCandidate(TypedDict, total=False):
    model: Required[str]
    """The model ID to evaluate."""

    sampling_params: Required[SamplingParamsParam]
    """The sampling parameters for the model."""

    type: Required[Literal["model"]]

    system_message: SystemMessageParam
    """(Optional) The system message providing instructions or context to the model."""


class EvalCandidateAgentCandidate(TypedDict, total=False):
    config: Required[AgentConfigParam]
    """The configuration for the agent candidate."""

    type: Required[Literal["agent"]]


EvalCandidate: TypeAlias = Union[EvalCandidateModelCandidate, EvalCandidateAgentCandidate]


class BenchmarkConfigParam(TypedDict, total=False):
    eval_candidate: Required[EvalCandidate]
    """The candidate to evaluate."""

    scoring_params: Required[Dict[str, ScoringFnParamsParam]]
    """
    Map between scoring function id and parameters for each scoring function you
    want to run
    """

    num_examples: int
    """(Optional) The number of examples to evaluate.

    If not provided, all examples in the dataset will be evaluated
    """

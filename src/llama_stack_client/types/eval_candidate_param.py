# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.agent_config import AgentConfig
from .shared_params.system_message import SystemMessage
from .shared_params.sampling_params import SamplingParams

__all__ = ["EvalCandidateParam", "ModelCandidate", "AgentCandidate"]


class ModelCandidate(TypedDict, total=False):
    model: Required[str]
    """The model ID to evaluate."""

    sampling_params: Required[SamplingParams]
    """The sampling parameters for the model."""

    type: Required[Literal["model"]]

    system_message: SystemMessage
    """(Optional) The system message providing instructions or context to the model."""


class AgentCandidate(TypedDict, total=False):
    config: Required[AgentConfig]
    """The configuration for the agent candidate."""

    type: Required[Literal["agent"]]


EvalCandidateParam: TypeAlias = Union[ModelCandidate, AgentCandidate]

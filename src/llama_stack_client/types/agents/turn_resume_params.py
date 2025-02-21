# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.tool_response_message import ToolResponseMessage

__all__ = ["TurnResumeParamsBase", "TurnResumeParamsNonStreaming", "TurnResumeParamsStreaming"]


class TurnResumeParamsBase(TypedDict, total=False):
    agent_id: Required[str]

    session_id: Required[str]

    tool_responses: Required[Iterable[ToolResponseMessage]]
    """The tool call responses to resume the turn with."""


class TurnResumeParamsNonStreaming(TurnResumeParamsBase, total=False):
    stream: Literal[False]
    """Whether to stream the response."""


class TurnResumeParamsStreaming(TurnResumeParamsBase):
    stream: Required[Literal[True]]
    """Whether to stream the response."""


TurnResumeParams = Union[TurnResumeParamsNonStreaming, TurnResumeParamsStreaming]

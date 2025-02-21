# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from ..shared_params.tool_response_message import ToolResponseMessage

__all__ = ["TurnContinueParamsBase", "TurnContinueParamsNonStreaming", "TurnContinueParamsStreaming"]


class TurnContinueParamsBase(TypedDict, total=False):
    agent_id: Required[str]

    session_id: Required[str]

    tool_responses: Required[Iterable[ToolResponseMessage]]


class TurnContinueParamsNonStreaming(TurnContinueParamsBase, total=False):
    stream: Literal[False]


class TurnContinueParamsStreaming(TurnContinueParamsBase):
    stream: Required[Literal[True]]


TurnContinueParams = Union[TurnContinueParamsNonStreaming, TurnContinueParamsStreaming]

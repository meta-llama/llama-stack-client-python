# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .tool_response_param import ToolResponseParam

__all__ = ["TurnResumeParams"]


class TurnResumeParams(TypedDict, total=False):
    agent_id: Required[str]

    session_id: Required[str]

    tool_responses: Required[Iterable[ToolResponseParam]]
    """The tool call responses to resume the turn with."""

    stream: bool
    """Whether to stream the response."""

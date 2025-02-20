# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

from ..shared_params.user_message import UserMessage
from ..shared_params.tool_response_message import ToolResponseMessage

__all__ = ["TurnContinueParams", "NewMessage"]


class TurnContinueParams(TypedDict, total=False):
    agent_id: Required[str]

    session_id: Required[str]

    new_messages: Required[Iterable[NewMessage]]


NewMessage: TypeAlias = Union[UserMessage, ToolResponseMessage]

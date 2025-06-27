# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .user_message import UserMessage
from .system_message import SystemMessage
from .completion_message import CompletionMessage
from .tool_response_message import ToolResponseMessage

__all__ = ["Message"]

Message: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ReturnType"]


class ReturnType(BaseModel):
    type: Literal[
        "string",
        "number",
        "boolean",
        "array",
        "object",
        "json",
        "union",
        "chat_completion_input",
        "completion_input",
        "agent_turn_input",
    ]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ReturnType"]


class ReturnType(TypedDict, total=False):
    type: Required[
        Literal[
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
    ]

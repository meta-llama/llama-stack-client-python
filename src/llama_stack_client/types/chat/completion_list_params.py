# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CompletionListParams"]


class CompletionListParams(TypedDict, total=False):
    after: str
    """The ID of the last chat completion to return."""

    limit: int
    """The maximum number of chat completions to return."""

    model: str
    """The model to filter by."""

    order: Literal["asc", "desc"]
    """The order to sort the chat completions by: "asc" or "desc". Defaults to "desc"."""

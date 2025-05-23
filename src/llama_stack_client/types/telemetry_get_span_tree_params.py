# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

__all__ = ["TelemetryGetSpanTreeParams"]


class TelemetryGetSpanTreeParams(TypedDict, total=False):
    attributes_to_return: List[str]
    """The attributes to return in the tree."""

    max_depth: int
    """The maximum depth of the tree."""

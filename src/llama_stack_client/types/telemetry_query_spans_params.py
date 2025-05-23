# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .query_condition_param import QueryConditionParam

__all__ = ["TelemetryQuerySpansParams"]


class TelemetryQuerySpansParams(TypedDict, total=False):
    attribute_filters: Required[Iterable[QueryConditionParam]]
    """The attribute filters to apply to the spans."""

    attributes_to_return: Required[List[str]]
    """The attributes to return in the spans."""

    max_depth: int
    """The maximum depth of the tree."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import TypedDict

from .query_condition_param import QueryConditionParam

__all__ = ["TelemetryQueryTracesParams"]


class TelemetryQueryTracesParams(TypedDict, total=False):
    attribute_filters: Iterable[QueryConditionParam]

    limit: int

    offset: int

    order_by: List[str]

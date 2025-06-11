# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .query_condition_param import QueryConditionParam

__all__ = ["TelemetrySaveSpansToDatasetParams"]


class TelemetrySaveSpansToDatasetParams(TypedDict, total=False):
    attribute_filters: Required[Iterable[QueryConditionParam]]

    attributes_to_save: Required[List[str]]

    dataset_id: Required[str]

    max_depth: int

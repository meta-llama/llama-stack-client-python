# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetioGetRowsPaginatedParams"]


class DatasetioGetRowsPaginatedParams(TypedDict, total=False):
    dataset_id: Required[str]

    rows_in_page: Required[int]

    filter_condition: str

    page_token: str

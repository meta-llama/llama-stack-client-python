# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DatasetioGetRowsPaginatedParams"]


class DatasetioGetRowsPaginatedParams(TypedDict, total=False):
    dataset_id: Required[str]
    """The ID of the dataset to get the rows from."""

    rows_in_page: Required[int]
    """The number of rows to get per page."""

    filter_condition: str
    """(Optional) A condition to filter the rows by."""

    page_token: str
    """The token to get the next page of rows."""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatasetioGetRowsPaginatedParams"]


class DatasetioGetRowsPaginatedParams(TypedDict, total=False):
    dataset_id: Required[str]

    rows_in_page: Required[int]

    filter_condition: str

    page_token: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

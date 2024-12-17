# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TelemetrySaveSpansToDatasetParams", "AttributeFilter"]


class TelemetrySaveSpansToDatasetParams(TypedDict, total=False):
    attribute_filters: Required[Iterable[AttributeFilter]]

    attributes_to_save: Required[List[str]]

    dataset_id: Required[str]

    max_depth: int

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class AttributeFilter(TypedDict, total=False):
    key: Required[str]

    op: Required[Literal["eq", "ne", "gt", "lt"]]

    value: Required[Union[bool, float, str, Iterable[object], object, None]]

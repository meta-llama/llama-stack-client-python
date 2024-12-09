# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TelemetryQueryTracesParams", "AttributeFilter"]


class TelemetryQueryTracesParams(TypedDict, total=False):
    attribute_filters: Iterable[AttributeFilter]

    limit: int

    offset: int

    order_by: List[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class AttributeFilter(TypedDict, total=False):
    key: Required[str]

    op: Required[Literal["eq", "ne", "gt", "lt"]]

    value: Required[Union[bool, float, str, Iterable[object], object, None]]

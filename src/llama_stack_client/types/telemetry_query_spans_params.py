# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .query_condition_param import QueryConditionParam

__all__ = ["TelemetryQuerySpansParams"]


class TelemetryQuerySpansParams(TypedDict, total=False):
    attribute_filters: Required[Iterable[QueryConditionParam]]

    attributes_to_return: Required[List[str]]

    max_depth: int

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]

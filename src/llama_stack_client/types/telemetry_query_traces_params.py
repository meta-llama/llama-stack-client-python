# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .query_condition_param import QueryConditionParam

__all__ = ["TelemetryQueryTracesParams"]


class TelemetryQueryTracesParams(TypedDict, total=False):
    attribute_filters: Iterable[QueryConditionParam]

    limit: int

    offset: int

    order_by: List[str]

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]

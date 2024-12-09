# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TelemetryGetSpanTreeParams"]


class TelemetryGetSpanTreeParams(TypedDict, total=False):
    span_id: Required[str]

    max_depth: int

    attributes_to_return: List[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

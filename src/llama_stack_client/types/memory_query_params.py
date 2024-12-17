# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.interleaved_content import InterleavedContent

__all__ = ["MemoryQueryParams"]


class MemoryQueryParams(TypedDict, total=False):
    bank_id: Required[str]

    query: Required[InterleavedContent]

    params: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

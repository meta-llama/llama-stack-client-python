# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .query_config_param import QueryConfigParam
from ..shared_params.interleaved_content import InterleavedContent

__all__ = ["RagToolQueryParams"]


class RagToolQueryParams(TypedDict, total=False):
    content: Required[InterleavedContent]

    vector_db_ids: Required[List[str]]

    query_config: QueryConfigParam

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]

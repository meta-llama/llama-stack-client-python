# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.interleaved_content import InterleavedContent

__all__ = ["VectorIoInsertParams", "Chunk"]


class VectorIoInsertParams(TypedDict, total=False):
    chunks: Required[Iterable[Chunk]]

    vector_db_id: Required[str]

    ttl_seconds: int

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]


class Chunk(TypedDict, total=False):
    content: Required[InterleavedContent]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

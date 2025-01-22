# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from .document_param import DocumentParam

__all__ = ["RagToolInsertParams"]


class RagToolInsertParams(TypedDict, total=False):
    chunk_size_in_tokens: Required[int]

    documents: Required[Iterable[DocumentParam]]

    vector_db_id: Required[str]

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]

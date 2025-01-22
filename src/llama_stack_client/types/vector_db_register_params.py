# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["VectorDBRegisterParams"]


class VectorDBRegisterParams(TypedDict, total=False):
    embedding_model: Required[str]

    vector_db_id: Required[str]

    embedding_dimension: int

    provider_id: str

    provider_vector_db_id: str

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]

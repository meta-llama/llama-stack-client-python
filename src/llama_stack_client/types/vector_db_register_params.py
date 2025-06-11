# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VectorDBRegisterParams"]


class VectorDBRegisterParams(TypedDict, total=False):
    embedding_model: Required[str]

    vector_db_id: Required[str]

    embedding_dimension: int

    provider_id: str

    provider_vector_db_id: str

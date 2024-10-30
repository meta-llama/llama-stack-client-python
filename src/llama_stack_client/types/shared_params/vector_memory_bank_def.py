# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VectorMemoryBankDef"]


class VectorMemoryBankDef(TypedDict, total=False):
    chunk_size_in_tokens: Required[int]

    embedding_model: Required[str]

    identifier: Required[str]

    provider_id: Required[str]

    type: Required[Literal["vector"]]

    overlap_size_in_tokens: int

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VectorMemoryBankDef"]


class VectorMemoryBankDef(BaseModel):
    chunk_size_in_tokens: int

    embedding_model: str

    identifier: str

    provider_id: str

    type: Literal["vector"]

    overlap_size_in_tokens: Optional[int] = None

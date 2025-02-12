# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.interleaved_content import InterleavedContent

__all__ = ["MemoryRetrievalStep"]


class MemoryRetrievalStep(BaseModel):
    inserted_context: InterleavedContent
    """A image content item"""

    step_id: str

    step_type: Literal["memory_retrieval"]

    turn_id: str

    vector_db_ids: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

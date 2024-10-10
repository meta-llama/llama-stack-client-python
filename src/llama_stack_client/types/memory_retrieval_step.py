# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.image_media import ImageMedia
from .shared.content_array import ContentArray

__all__ = ["MemoryRetrievalStep", "InsertedContext"]

InsertedContext: TypeAlias = Union[str, ImageMedia, ContentArray]


class MemoryRetrievalStep(BaseModel):
    inserted_context: InsertedContext

    memory_bank_ids: List[str]

    step_id: str

    step_type: Literal["memory_retrieval"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

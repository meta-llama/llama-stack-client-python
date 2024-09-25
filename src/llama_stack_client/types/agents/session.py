# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .turn import Turn
from ..._models import BaseModel

__all__ = ["Session"]


class Session(BaseModel):
    session_id: str

    session_name: str

    started_at: datetime

    turns: List[Turn]

    memory_bank: Optional[object] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["Trace"]


class Trace(BaseModel):
    root_span_id: str

    start_time: datetime

    trace_id: str

    end_time: Optional[datetime] = None

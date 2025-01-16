# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TelemetryGetSpanResponse"]


class TelemetryGetSpanResponse(BaseModel):
    name: str

    span_id: str

    start_time: datetime

    trace_id: str

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    end_time: Optional[datetime] = None

    parent_span_id: Optional[str] = None

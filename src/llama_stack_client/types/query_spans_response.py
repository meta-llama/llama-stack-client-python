# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["QuerySpansResponse", "Data", "Metric"]


class Data(BaseModel):
    name: str

    span_id: str

    start_time: datetime

    trace_id: str

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    end_time: Optional[datetime] = None

    parent_span_id: Optional[str] = None


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class QuerySpansResponse(BaseModel):
    data: List[Data]

    metrics: Optional[List[Metric]] = None

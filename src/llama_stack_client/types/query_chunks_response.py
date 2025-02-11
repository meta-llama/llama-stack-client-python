# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.interleaved_content import InterleavedContent

__all__ = ["QueryChunksResponse", "Chunk", "Metric"]


class Chunk(BaseModel):
    content: InterleavedContent
    """A image content item"""

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class QueryChunksResponse(BaseModel):
    chunks: List[Chunk]

    scores: List[float]

    metrics: Optional[List[Metric]] = None

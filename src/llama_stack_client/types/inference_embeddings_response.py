# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .embeddings_response import EmbeddingsResponse

__all__ = ["InferenceEmbeddingsResponse", "Metric"]


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class InferenceEmbeddingsResponse(BaseModel):
    data: EmbeddingsResponse
    """Response containing generated embeddings."""

    metrics: Optional[List[Metric]] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmbeddingsResponse", "Metric"]


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class EmbeddingsResponse(BaseModel):
    embeddings: List[List[float]]
    """List of embedding vectors, one per input content.

    Each embedding is a list of floats. The dimensionality of the embedding is
    model-specific; you can check model metadata using /models/{model_id}
    """

    metrics: Optional[List[Metric]] = None

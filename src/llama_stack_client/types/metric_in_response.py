# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MetricInResponse"]


class MetricInResponse(BaseModel):
    metric: str

    value: float

    unit: Optional[str] = None

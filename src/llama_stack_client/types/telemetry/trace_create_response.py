# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .trace import Trace
from ..._models import BaseModel

__all__ = ["TraceCreateResponse"]


class TraceCreateResponse(BaseModel):
    data: List[Trace]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .span import Span
from ..._models import BaseModel

__all__ = ["SpanCreateResponse"]


class SpanCreateResponse(BaseModel):
    data: List[Span]

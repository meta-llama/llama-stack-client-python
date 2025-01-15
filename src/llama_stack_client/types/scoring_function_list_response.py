# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .scoring_fn import ScoringFn

__all__ = ["ScoringFunctionListResponse"]


class ScoringFunctionListResponse(BaseModel):
    data: List[ScoringFn]

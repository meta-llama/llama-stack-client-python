# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .benchmark import Benchmark

__all__ = ["BenchmarkListResponse"]


class BenchmarkListResponse(BaseModel):
    data: List[Benchmark]

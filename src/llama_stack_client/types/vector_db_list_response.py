# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .vector_db import VectorDB

__all__ = ["VectorDBListResponse"]


class VectorDBListResponse(BaseModel):
    data: List[VectorDB]

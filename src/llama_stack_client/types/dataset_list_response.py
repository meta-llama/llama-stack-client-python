# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .dataset import Dataset
from .._models import BaseModel

__all__ = ["DatasetListResponse"]


class DatasetListResponse(BaseModel):
    data: List[Dataset]

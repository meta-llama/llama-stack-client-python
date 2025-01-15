# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["JobListResponse", "Data"]


class Data(BaseModel):
    job_uuid: str


class JobListResponse(BaseModel):
    data: List[Data]

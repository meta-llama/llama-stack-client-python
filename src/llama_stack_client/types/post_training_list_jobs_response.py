# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["PostTrainingListJobsResponse", "Data"]


class Data(BaseModel):
    job_uuid: str


class PostTrainingListJobsResponse(BaseModel):
    data: List[Data]

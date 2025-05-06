# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["InspectListRoutesResponse", "Data"]


class Data(BaseModel):
    method: str

    provider_types: List[str]

    route: str


class InspectListRoutesResponse(BaseModel):
    data: List[Data]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["V1ListModelsResponse", "Data"]


class Data(BaseModel):
    id: str

    created: int

    object: Literal["model"]

    owned_by: str


class V1ListModelsResponse(BaseModel):
    data: List[Data]

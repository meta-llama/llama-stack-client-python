# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ListVectorDBsResponse", "Data"]


class Data(BaseModel):
    embedding_dimension: int

    embedding_model: str

    identifier: str

    provider_id: str

    provider_resource_id: str

    type: Literal["vector_db"]


class ListVectorDBsResponse(BaseModel):
    data: List[Data]
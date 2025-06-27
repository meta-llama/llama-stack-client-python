# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VectorStoreSearchResponse", "Data", "DataContent"]


class DataContent(BaseModel):
    text: str

    type: Literal["text"]


class Data(BaseModel):
    content: List[DataContent]

    file_id: str

    filename: str

    score: float

    attributes: Optional[Dict[str, Union[str, float, bool]]] = None


class VectorStoreSearchResponse(BaseModel):
    data: List[Data]

    has_more: bool

    object: str

    search_query: str

    next_page: Optional[str] = None

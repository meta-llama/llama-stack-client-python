# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["VectorStoreSearchResponse"]


class VectorStoreSearchResponse(BaseModel):
    data: List[Dict[str, Union[bool, float, str, List[object], object, None]]]

    has_more: bool

    object: str

    search_query: str

    next_page: Optional[str] = None

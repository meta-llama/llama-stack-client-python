# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["PaginatedRowsResult"]


class PaginatedRowsResult(BaseModel):
    rows: List[Dict[str, Union[bool, float, str, List[object], object, None]]]

    total_count: int

    next_page_token: Optional[str] = None

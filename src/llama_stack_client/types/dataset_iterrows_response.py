# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["DatasetIterrowsResponse"]


class DatasetIterrowsResponse(BaseModel):
    data: List[Dict[str, Union[bool, float, str, List[object], object, None]]]
    """The rows in the current page."""

    next_start_index: Optional[int] = None
    """Index into dataset for the first row in the next page.

    None if there are no more rows.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .shield import Shield
from .._models import BaseModel

__all__ = ["ListShieldsResponse"]


class ListShieldsResponse(BaseModel):
    data: List[Shield]

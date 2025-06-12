# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .file import File
from .._models import BaseModel

__all__ = ["ListFilesResponse"]


class ListFilesResponse(BaseModel):
    data: List[File]
    """List of file objects"""

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]
    """The object type, which is always "list" """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["FileListResponse", "Data"]


class Data(BaseModel):
    name: str


class FileListResponse(BaseModel):
    data: List[Data]
    """List of FileResponse entries"""

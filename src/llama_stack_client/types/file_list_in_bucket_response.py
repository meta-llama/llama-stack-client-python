# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .file import File
from .._models import BaseModel

__all__ = ["FileListInBucketResponse"]


class FileListInBucketResponse(BaseModel):
    data: List[File]
    """List of FileResponse entries"""

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["FileUpload"]


class FileUpload(BaseModel):
    id: str
    """ID of the upload session"""

    offset: int
    """Upload content offset"""

    size: int
    """Upload content size"""

    url: str
    """Upload URL for the file or file parts"""

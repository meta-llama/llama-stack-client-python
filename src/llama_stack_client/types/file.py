# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    bucket: str
    """Bucket under which the file is stored (valid chars: a-zA-Z0-9\\__-)"""

    bytes: int
    """Size of the file in bytes"""

    created_at: int
    """Timestamp of when the file was created"""

    key: str
    """Key under which the file is stored (valid chars: a-zA-Z0-9\\__-/.)"""

    mime_type: str
    """MIME type of the file"""

    url: str
    """Upload URL for the file contents"""

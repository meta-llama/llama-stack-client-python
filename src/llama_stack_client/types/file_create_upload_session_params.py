# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileCreateUploadSessionParams"]


class FileCreateUploadSessionParams(TypedDict, total=False):
    bucket: Required[str]
    """Bucket under which the file is stored (valid chars: a-zA-Z0-9\\__-)"""

    key: Required[str]
    """Key under which the file is stored (valid chars: a-zA-Z0-9\\__-/.)"""

    mime_type: Required[str]
    """MIME type of the file"""

    size: Required[int]
    """File size in bytes"""

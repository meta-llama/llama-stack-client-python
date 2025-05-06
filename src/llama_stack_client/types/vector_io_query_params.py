# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .interleaved_content_param import InterleavedContentParam

__all__ = ["VectorIoQueryParams"]


class VectorIoQueryParams(TypedDict, total=False):
    query: Required[InterleavedContentParam]
    """A image content item"""

    vector_db_id: Required[str]

    params: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

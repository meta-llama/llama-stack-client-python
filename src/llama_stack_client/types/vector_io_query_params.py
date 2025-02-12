# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.interleaved_content import InterleavedContent

__all__ = ["VectorIoQueryParams"]


class VectorIoQueryParams(TypedDict, total=False):
    query: Required[InterleavedContent]
    """A image content item"""

    vector_db_id: Required[str]

    params: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .image_media import ImageMedia

__all__ = ["SystemMessage", "Content", "ContentImageMediaArray"]

ContentImageMediaArray: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentImageMediaArray]]


class SystemMessage(TypedDict, total=False):
    content: Required[Content]

    role: Required[Literal["system"]]

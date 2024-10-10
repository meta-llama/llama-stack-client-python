# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import TypeAlias

from .image_media import ImageMedia

__all__ = ["ContentArray", "ContentArrayItem"]

ContentArrayItem: TypeAlias = Union[str, ImageMedia]

ContentArray: TypeAlias = List[ContentArrayItem]

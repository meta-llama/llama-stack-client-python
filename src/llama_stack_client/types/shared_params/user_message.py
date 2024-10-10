# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .image_media import ImageMedia

__all__ = ["UserMessage", "Content", "ContentUnionMember2", "Context", "ContextUnionMember2"]

ContentUnionMember2: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentUnionMember2]]

ContextUnionMember2: TypeAlias = Union[str, ImageMedia]

Context: TypeAlias = Union[str, ImageMedia, List[ContextUnionMember2]]


class UserMessage(TypedDict, total=False):
    content: Required[Content]

    role: Required[Literal["user"]]

    context: Context

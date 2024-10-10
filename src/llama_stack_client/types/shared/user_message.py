# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .image_media import ImageMedia

__all__ = ["UserMessage", "Content", "ContentUnionMember2", "Context", "ContextUnionMember2"]

ContentUnionMember2: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentUnionMember2]]

ContextUnionMember2: TypeAlias = Union[str, ImageMedia]

Context: TypeAlias = Union[str, ImageMedia, List[ContextUnionMember2]]


class UserMessage(BaseModel):
    content: Content

    role: Literal["user"]

    context: Optional[Context] = None

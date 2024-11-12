# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .image_media import ImageMedia

__all__ = ["UserMessage", "Content", "ContentImageMediaArray", "Context", "ContextImageMediaArray"]

ContentImageMediaArray: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentImageMediaArray]]

ContextImageMediaArray: TypeAlias = Union[str, ImageMedia]

Context: TypeAlias = Union[str, ImageMedia, List[ContextImageMediaArray]]


class UserMessage(BaseModel):
    content: Content

    role: Literal["user"]

    context: Optional[Context] = None

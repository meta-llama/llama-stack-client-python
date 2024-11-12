# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .image_media import ImageMedia

__all__ = ["Attachment", "Content", "ContentContentArray"]

ContentContentArray: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentContentArray]]


class Attachment(BaseModel):
    content: Content

    mime_type: str

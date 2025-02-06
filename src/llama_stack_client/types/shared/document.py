# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .url import URL
from ..._models import BaseModel
from .interleaved_content_item import InterleavedContentItem

__all__ = ["Document", "Content", "ContentImageContentItem", "ContentImageContentItemImage", "ContentTextContentItem"]


class ContentImageContentItemImage(BaseModel):
    data: Optional[str] = None
    """base64 encoded image data as string"""

    url: Optional[URL] = None
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ContentImageContentItem(BaseModel):
    image: ContentImageContentItemImage
    """Image as a base64 encoded string or an URL"""

    type: Literal["image"]
    """Discriminator type of the content item. Always "image" """


class ContentTextContentItem(BaseModel):
    text: str
    """Text content"""

    type: Literal["text"]
    """Discriminator type of the content item. Always "text" """


Content: TypeAlias = Union[str, ContentImageContentItem, ContentTextContentItem, List[InterleavedContentItem], URL]


class Document(BaseModel):
    content: Content
    """A image content item"""

    document_id: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    mime_type: Optional[str] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .url import URL
from .interleaved_content_item import InterleavedContentItem

__all__ = ["Document", "Content", "ContentImageContentItem", "ContentImageContentItemImage", "ContentTextContentItem"]


class ContentImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: URL
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class ContentImageContentItem(TypedDict, total=False):
    image: Required[ContentImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class ContentTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


Content: TypeAlias = Union[str, ContentImageContentItem, ContentTextContentItem, Iterable[InterleavedContentItem], URL]


class Document(TypedDict, total=False):
    content: Required[Content]
    """A image content item"""

    document_id: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    mime_type: str

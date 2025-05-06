# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..url_param import URLParam
from ..interleaved_content_item_param import InterleavedContentItemParam

__all__ = [
    "RagToolInsertDocumentsParams",
    "Document",
    "DocumentContent",
    "DocumentContentImageContentItem",
    "DocumentContentImageContentItemImage",
    "DocumentContentTextContentItem",
]


class RagToolInsertDocumentsParams(TypedDict, total=False):
    chunk_size_in_tokens: Required[int]

    documents: Required[Iterable[Document]]

    vector_db_id: Required[str]


class DocumentContentImageContentItemImage(TypedDict, total=False):
    data: str
    """base64 encoded image data as string"""

    url: URLParam
    """A URL of the image or data URL in the format of data:image/{type};base64,{data}.

    Note that URL could have length limits.
    """


class DocumentContentImageContentItem(TypedDict, total=False):
    image: Required[DocumentContentImageContentItemImage]
    """Image as a base64 encoded string or an URL"""

    type: Required[Literal["image"]]
    """Discriminator type of the content item. Always "image" """


class DocumentContentTextContentItem(TypedDict, total=False):
    text: Required[str]
    """Text content"""

    type: Required[Literal["text"]]
    """Discriminator type of the content item. Always "text" """


DocumentContent: TypeAlias = Union[
    str,
    DocumentContentImageContentItem,
    DocumentContentTextContentItem,
    Iterable[InterleavedContentItemParam],
    URLParam,
]


class Document(TypedDict, total=False):
    content: Required[DocumentContent]
    """The content of the document."""

    document_id: Required[str]
    """The unique identifier for the document."""

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """Additional metadata for the document."""

    mime_type: str
    """The MIME type of the document."""

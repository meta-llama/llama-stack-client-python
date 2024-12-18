# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.url import URL
from .shared_params.interleaved_content_item import InterleavedContentItem

__all__ = [
    "MemoryInsertParams",
    "Document",
    "DocumentContent",
    "DocumentContentImageContentItem",
    "DocumentContentTextContentItem",
]


class MemoryInsertParams(TypedDict, total=False):
    bank_id: Required[str]

    documents: Required[Iterable[Document]]

    ttl_seconds: int

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class DocumentContentImageContentItem(TypedDict, total=False):
    type: Required[Literal["image"]]

    data: str

    url: URL


class DocumentContentTextContentItem(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]


DocumentContent: TypeAlias = Union[
    str, DocumentContentImageContentItem, DocumentContentTextContentItem, Iterable[InterleavedContentItem], URL
]


class Document(TypedDict, total=False):
    content: Required[DocumentContent]

    document_id: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    mime_type: str

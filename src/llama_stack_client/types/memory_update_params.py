# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.image_media import ImageMedia
from .shared_params.content_array import ContentArray

__all__ = ["MemoryUpdateParams", "Document", "DocumentContent"]


class MemoryUpdateParams(TypedDict, total=False):
    bank_id: Required[str]

    documents: Required[Iterable[Document]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


DocumentContent: TypeAlias = Union[str, ImageMedia, ContentArray]


class Document(TypedDict, total=False):
    content: Required[DocumentContent]

    document_id: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    mime_type: str

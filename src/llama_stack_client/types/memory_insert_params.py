# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.image_media import ImageMedia

__all__ = ["MemoryInsertParams", "Document", "DocumentContent", "DocumentContentUnionMember2"]


class MemoryInsertParams(TypedDict, total=False):
    bank_id: Required[str]

    documents: Required[Iterable[Document]]

    ttl_seconds: int

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


DocumentContentUnionMember2: TypeAlias = Union[str, ImageMedia]

DocumentContent: TypeAlias = Union[str, ImageMedia, List[DocumentContentUnionMember2]]


class Document(TypedDict, total=False):
    content: Required[DocumentContent]

    document_id: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    mime_type: str

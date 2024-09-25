# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MemoryUpdateParams",
    "Document",
    "DocumentContent",
    "DocumentContentImageMedia",
    "DocumentContentImageMediaImage",
    "DocumentContentImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "DocumentContentUnionMember2",
    "DocumentContentUnionMember2ImageMedia",
    "DocumentContentUnionMember2ImageMediaImage",
    "DocumentContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
]


class MemoryUpdateParams(TypedDict, total=False):
    bank_id: Required[str]

    documents: Required[Iterable[Document]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class DocumentContentImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


DocumentContentImageMediaImage: TypeAlias = Union[
    DocumentContentImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class DocumentContentImageMedia(TypedDict, total=False):
    image: Required[DocumentContentImageMediaImage]


class DocumentContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


DocumentContentUnionMember2ImageMediaImage: TypeAlias = Union[
    DocumentContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class DocumentContentUnionMember2ImageMedia(TypedDict, total=False):
    image: Required[DocumentContentUnionMember2ImageMediaImage]


DocumentContentUnionMember2: TypeAlias = Union[str, DocumentContentUnionMember2ImageMedia]

DocumentContent: TypeAlias = Union[str, DocumentContentImageMedia, List[DocumentContentUnionMember2]]


class Document(TypedDict, total=False):
    content: Required[DocumentContent]

    document_id: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    mime_type: str

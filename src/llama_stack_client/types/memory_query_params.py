# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MemoryQueryParams",
    "Query",
    "QueryImageMedia",
    "QueryImageMediaImage",
    "QueryImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "QueryUnionMember2",
    "QueryUnionMember2ImageMedia",
    "QueryUnionMember2ImageMediaImage",
    "QueryUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
]


class MemoryQueryParams(TypedDict, total=False):
    bank_id: Required[str]

    query: Required[Query]

    params: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class QueryImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


QueryImageMediaImage: TypeAlias = Union[QueryImageMediaImageThisClassRepresentsAnImageObjectToCreate, str]


class QueryImageMedia(TypedDict, total=False):
    image: Required[QueryImageMediaImage]


class QueryUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(TypedDict, total=False):
    format: str

    format_description: str


QueryUnionMember2ImageMediaImage: TypeAlias = Union[
    QueryUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class QueryUnionMember2ImageMedia(TypedDict, total=False):
    image: Required[QueryUnionMember2ImageMediaImage]


QueryUnionMember2: TypeAlias = Union[str, QueryUnionMember2ImageMedia]

Query: TypeAlias = Union[str, QueryImageMedia, List[QueryUnionMember2]]

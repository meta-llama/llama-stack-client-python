# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.image_media import ImageMedia

__all__ = ["MemoryQueryParams", "Query", "QueryUnionMember2"]


class MemoryQueryParams(TypedDict, total=False):
    bank_id: Required[str]

    query: Required[Query]

    params: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


QueryUnionMember2: TypeAlias = Union[str, ImageMedia]

Query: TypeAlias = Union[str, ImageMedia, List[QueryUnionMember2]]

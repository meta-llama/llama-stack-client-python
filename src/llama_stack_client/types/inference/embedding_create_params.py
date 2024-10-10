# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..shared_params.image_media import ImageMedia
from ..shared_params.content_array import ContentArray

__all__ = ["EmbeddingCreateParams", "Content"]


class EmbeddingCreateParams(TypedDict, total=False):
    contents: Required[List[Content]]

    model: Required[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


Content: TypeAlias = Union[str, ImageMedia, ContentArray]

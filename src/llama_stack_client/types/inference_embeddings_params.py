# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.interleaved_content import InterleavedContent

__all__ = ["InferenceEmbeddingsParams"]


class InferenceEmbeddingsParams(TypedDict, total=False):
    contents: Required[List[InterleavedContent]]

    model_id: Required[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

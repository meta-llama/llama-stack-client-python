# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .shared_params.interleaved_content import InterleavedContent

__all__ = ["InferenceEmbeddingsParams"]


class InferenceEmbeddingsParams(TypedDict, total=False):
    contents: Required[List[InterleavedContent]]
    """List of contents to generate embeddings for.

    Note that content can be multimodal. The behavior depends on the model and
    provider. Some models may only support text.
    """

    model_id: Required[str]
    """The identifier of the model to use.

    The model must be an embedding model registered with Llama Stack and available
    via the /models endpoint.
    """

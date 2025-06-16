# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["EmbeddingsResponse"]


class EmbeddingsResponse(BaseModel):
    embeddings: List[List[float]]
    """List of embedding vectors, one per input content.

    Each embedding is a list of floats. The dimensionality of the embedding is
    model-specific; you can check model metadata using /models/{model_id}
    """

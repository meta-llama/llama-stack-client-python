# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["VectorStoreDeleteResponse"]


class VectorStoreDeleteResponse(BaseModel):
    id: str

    deleted: bool

    object: str

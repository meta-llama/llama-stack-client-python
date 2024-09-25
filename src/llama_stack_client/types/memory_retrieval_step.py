# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "MemoryRetrievalStep",
    "InsertedContext",
    "InsertedContextImageMedia",
    "InsertedContextImageMediaImage",
    "InsertedContextImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "InsertedContextUnionMember2",
    "InsertedContextUnionMember2ImageMedia",
    "InsertedContextUnionMember2ImageMediaImage",
    "InsertedContextUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
]


class InsertedContextImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


InsertedContextImageMediaImage: TypeAlias = Union[
    InsertedContextImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class InsertedContextImageMedia(BaseModel):
    image: InsertedContextImageMediaImage


class InsertedContextUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


InsertedContextUnionMember2ImageMediaImage: TypeAlias = Union[
    InsertedContextUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class InsertedContextUnionMember2ImageMedia(BaseModel):
    image: InsertedContextUnionMember2ImageMediaImage


InsertedContextUnionMember2: TypeAlias = Union[str, InsertedContextUnionMember2ImageMedia]

InsertedContext: TypeAlias = Union[str, InsertedContextImageMedia, List[InsertedContextUnionMember2]]


class MemoryRetrievalStep(BaseModel):
    inserted_context: InsertedContext

    memory_bank_ids: List[str]

    step_id: str

    step_type: Literal["memory_retrieval"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

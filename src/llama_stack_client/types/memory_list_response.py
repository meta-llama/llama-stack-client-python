# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "MemoryListResponse",
    "Config",
    "ConfigMemoryBankConfigVectorType",
    "ConfigMemoryBankConfigKeyValueType",
    "ConfigMemoryBankConfigKeywordType",
    "ConfigMemoryBankConfigGraphType",
]


class ConfigMemoryBankConfigVectorType(BaseModel):
    chunk_size_in_tokens: int

    embedding_model: str

    type: Literal["vector"]

    overlap_size_in_tokens: Optional[int] = None


class ConfigMemoryBankConfigKeyValueType(BaseModel):
    type: Literal["keyvalue"]


class ConfigMemoryBankConfigKeywordType(BaseModel):
    type: Literal["keyword"]


class ConfigMemoryBankConfigGraphType(BaseModel):
    type: Literal["graph"]


Config: TypeAlias = Annotated[
    Union[
        ConfigMemoryBankConfigVectorType,
        ConfigMemoryBankConfigKeyValueType,
        ConfigMemoryBankConfigKeywordType,
        ConfigMemoryBankConfigGraphType,
    ],
    PropertyInfo(discriminator="type"),
]


class MemoryListResponse(BaseModel):
    bank_id: str

    config: Config

    name: str

    url: Optional[str] = None

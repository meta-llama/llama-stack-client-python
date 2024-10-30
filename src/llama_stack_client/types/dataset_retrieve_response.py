# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["DatasetRetrieveResponse", "DatasetSchema", "DatasetSchemaType"]


class DatasetSchemaType(BaseModel):
    type: Literal["string"]


DatasetSchema: TypeAlias = Union[
    DatasetSchemaType,
    DatasetSchemaType,
    DatasetSchemaType,
    DatasetSchemaType,
    DatasetSchemaType,
    DatasetSchemaType,
    DatasetSchemaType,
    DatasetSchemaType,
    DatasetSchemaType,
    DatasetSchemaType,
]


class DatasetRetrieveResponse(BaseModel):
    dataset_schema: Dict[str, DatasetSchema]

    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    url: str

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["DatasetListResponse", "Schema", "SchemaType"]


class SchemaType(BaseModel):
    type: Literal["string"]


Schema: TypeAlias = Union[
    SchemaType,
    SchemaType,
    SchemaType,
    SchemaType,
    SchemaType,
    SchemaType,
    SchemaType,
    SchemaType,
    SchemaType,
    SchemaType,
]


class DatasetListResponse(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    provider_resource_id: str

    schema_: Dict[str, Schema] = FieldInfo(alias="schema")

    type: Literal["dataset"]

    url: str

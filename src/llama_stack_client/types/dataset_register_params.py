# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatasetRegisterParams", "DatasetDef", "DatasetDefDatasetSchema", "DatasetDefDatasetSchemaType"]


class DatasetRegisterParams(TypedDict, total=False):
    dataset_def: Required[DatasetDef]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class DatasetDefDatasetSchemaType(TypedDict, total=False):
    type: Required[Literal["string"]]


DatasetDefDatasetSchema: TypeAlias = Union[
    DatasetDefDatasetSchemaType,
    DatasetDefDatasetSchemaType,
    DatasetDefDatasetSchemaType,
    DatasetDefDatasetSchemaType,
    DatasetDefDatasetSchemaType,
    DatasetDefDatasetSchemaType,
    DatasetDefDatasetSchemaType,
    DatasetDefDatasetSchemaType,
    DatasetDefDatasetSchemaType,
    DatasetDefDatasetSchemaType,
]


class DatasetDef(TypedDict, total=False):
    dataset_schema: Required[Dict[str, DatasetDefDatasetSchema]]

    identifier: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    provider_id: Required[str]

    url: Required[str]

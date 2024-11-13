# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["DatasetRegisterParams", "DatasetSchema", "DatasetSchemaType"]


class DatasetRegisterParams(TypedDict, total=False):
    dataset_id: Required[str]

    dataset_schema: Required[Dict[str, DatasetSchema]]

    url: Required[str]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    provider_dataset_id: str

    provider_id: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class DatasetSchemaType(TypedDict, total=False):
    type: Required[Literal["string"]]


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

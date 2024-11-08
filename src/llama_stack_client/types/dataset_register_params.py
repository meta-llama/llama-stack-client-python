# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "DatasetRegisterParams",
    "DatasetDef",
    "DatasetDefDatasetSchema",
    "DatasetDefDatasetSchemaDsString",
    "DatasetDefDatasetSchemaDsNumber",
    "DatasetDefDatasetSchemaDsBoolean",
    "DatasetDefDatasetSchemaDsArray",
    "DatasetDefDatasetSchemaDsObject",
    "DatasetDefDatasetSchemaDsJson",
    "DatasetDefDatasetSchemaDsUnion",
    "DatasetDefDatasetSchemaDsChatCompletionInput",
    "DatasetDefDatasetSchemaDsCompletionInput",
    "DatasetDefDatasetSchemaDsAgentTurnInput",
]


class DatasetRegisterParams(TypedDict, total=False):
    dataset_def: Required[DatasetDef]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class DatasetDefDatasetSchemaDsString(TypedDict, total=False):
    type: Required[Literal["string"]]


class DatasetDefDatasetSchemaDsNumber(TypedDict, total=False):
    type: Required[Literal["number"]]


class DatasetDefDatasetSchemaDsBoolean(TypedDict, total=False):
    type: Required[Literal["boolean"]]


class DatasetDefDatasetSchemaDsArray(TypedDict, total=False):
    type: Required[Literal["array"]]


class DatasetDefDatasetSchemaDsObject(TypedDict, total=False):
    type: Required[Literal["object"]]


class DatasetDefDatasetSchemaDsJson(TypedDict, total=False):
    type: Required[Literal["json"]]


class DatasetDefDatasetSchemaDsUnion(TypedDict, total=False):
    type: Required[Literal["union"]]


class DatasetDefDatasetSchemaDsChatCompletionInput(TypedDict, total=False):
    type: Required[Literal["chat_completion_input"]]


class DatasetDefDatasetSchemaDsCompletionInput(TypedDict, total=False):
    type: Required[Literal["completion_input"]]


class DatasetDefDatasetSchemaDsAgentTurnInput(TypedDict, total=False):
    type: Required[Literal["agent_turn_input"]]


DatasetDefDatasetSchema: TypeAlias = Union[
    DatasetDefDatasetSchemaDsString,
    DatasetDefDatasetSchemaDsNumber,
    DatasetDefDatasetSchemaDsBoolean,
    DatasetDefDatasetSchemaDsArray,
    DatasetDefDatasetSchemaDsObject,
    DatasetDefDatasetSchemaDsJson,
    DatasetDefDatasetSchemaDsUnion,
    DatasetDefDatasetSchemaDsChatCompletionInput,
    DatasetDefDatasetSchemaDsCompletionInput,
    DatasetDefDatasetSchemaDsAgentTurnInput,
]


class DatasetDef(TypedDict, total=False):
    dataset_schema: Required[Dict[str, DatasetDefDatasetSchema]]

    identifier: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    provider_id: Required[str]

    type: Required[Literal["dataset"]]

    url: Required[str]

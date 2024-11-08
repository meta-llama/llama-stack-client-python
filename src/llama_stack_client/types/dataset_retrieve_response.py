# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "DatasetRetrieveResponse",
    "DatasetSchema",
    "DatasetSchemaDsString",
    "DatasetSchemaDsNumber",
    "DatasetSchemaDsBoolean",
    "DatasetSchemaDsArray",
    "DatasetSchemaDsObject",
    "DatasetSchemaDsJson",
    "DatasetSchemaDsUnion",
    "DatasetSchemaDsChatCompletionInput",
    "DatasetSchemaDsCompletionInput",
    "DatasetSchemaDsAgentTurnInput",
]


class DatasetSchemaDsString(BaseModel):
    type: Literal["string"]


class DatasetSchemaDsNumber(BaseModel):
    type: Literal["number"]


class DatasetSchemaDsBoolean(BaseModel):
    type: Literal["boolean"]


class DatasetSchemaDsArray(BaseModel):
    type: Literal["array"]


class DatasetSchemaDsObject(BaseModel):
    type: Literal["object"]


class DatasetSchemaDsJson(BaseModel):
    type: Literal["json"]


class DatasetSchemaDsUnion(BaseModel):
    type: Literal["union"]


class DatasetSchemaDsChatCompletionInput(BaseModel):
    type: Literal["chat_completion_input"]


class DatasetSchemaDsCompletionInput(BaseModel):
    type: Literal["completion_input"]


class DatasetSchemaDsAgentTurnInput(BaseModel):
    type: Literal["agent_turn_input"]


DatasetSchema: TypeAlias = Union[
    DatasetSchemaDsString,
    DatasetSchemaDsNumber,
    DatasetSchemaDsBoolean,
    DatasetSchemaDsArray,
    DatasetSchemaDsObject,
    DatasetSchemaDsJson,
    DatasetSchemaDsUnion,
    DatasetSchemaDsChatCompletionInput,
    DatasetSchemaDsCompletionInput,
    DatasetSchemaDsAgentTurnInput,
]


class DatasetRetrieveResponse(BaseModel):
    dataset_schema: Dict[str, DatasetSchema]

    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    type: Literal["dataset"]

    url: str

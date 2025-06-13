# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "InputItemListResponse",
    "Data",
    "DataOpenAIResponseOutputMessageWebSearchToolCall",
    "DataOpenAIResponseOutputMessageFileSearchToolCall",
    "DataOpenAIResponseOutputMessageFunctionToolCall",
    "DataOpenAIResponseInputFunctionToolCallOutput",
    "DataOpenAIResponseMessage",
    "DataOpenAIResponseMessageContentUnionMember1",
    "DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "DataOpenAIResponseMessageContentUnionMember2",
]


class DataOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Literal["web_search_call"]


class DataOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str

    queries: List[str]

    status: str

    type: Literal["file_search_call"]

    results: Optional[List[Dict[str, Union[bool, float, str, List[object], object, None]]]] = None


class DataOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str

    call_id: str

    name: str

    type: Literal["function_call"]

    id: Optional[str] = None

    status: Optional[str] = None


class DataOpenAIResponseInputFunctionToolCallOutput(BaseModel):
    call_id: str

    output: str

    type: Literal["function_call_output"]

    id: Optional[str] = None

    status: Optional[str] = None


class DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str

    type: Literal["input_text"]


class DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]

    type: Literal["input_image"]

    image_url: Optional[str] = None


DataOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        DataOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOpenAIResponseMessageContentUnionMember2(BaseModel):
    text: str

    type: Literal["output_text"]


class DataOpenAIResponseMessage(BaseModel):
    content: Union[
        str, List[DataOpenAIResponseMessageContentUnionMember1], List[DataOpenAIResponseMessageContentUnionMember2]
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


Data: TypeAlias = Union[
    DataOpenAIResponseOutputMessageWebSearchToolCall,
    DataOpenAIResponseOutputMessageFileSearchToolCall,
    DataOpenAIResponseOutputMessageFunctionToolCall,
    DataOpenAIResponseInputFunctionToolCallOutput,
    DataOpenAIResponseMessage,
]


class InputItemListResponse(BaseModel):
    data: List[Data]

    object: Literal["list"]

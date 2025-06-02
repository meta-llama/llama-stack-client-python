# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResponseListResponse",
    "Data",
    "DataInput",
    "DataInputOpenAIResponseOutputMessageWebSearchToolCall",
    "DataInputOpenAIResponseOutputMessageFunctionToolCall",
    "DataInputOpenAIResponseInputFunctionToolCallOutput",
    "DataInputOpenAIResponseMessage",
    "DataInputOpenAIResponseMessageContentUnionMember1",
    "DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "DataInputOpenAIResponseMessageContentUnionMember2",
    "DataOutput",
    "DataOutputOpenAIResponseMessage",
    "DataOutputOpenAIResponseMessageContentUnionMember1",
    "DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "DataOutputOpenAIResponseMessageContentUnionMember2",
    "DataOutputOpenAIResponseOutputMessageWebSearchToolCall",
    "DataOutputOpenAIResponseOutputMessageFunctionToolCall",
    "DataOutputOpenAIResponseOutputMessageMcpCall",
    "DataOutputOpenAIResponseOutputMessageMcpListTools",
    "DataOutputOpenAIResponseOutputMessageMcpListToolsTool",
    "DataError",
]


class DataInputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Literal["web_search_call"]


class DataInputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str

    call_id: str

    name: str

    type: Literal["function_call"]

    id: Optional[str] = None

    status: Optional[str] = None


class DataInputOpenAIResponseInputFunctionToolCallOutput(BaseModel):
    call_id: str

    output: str

    type: Literal["function_call_output"]

    id: Optional[str] = None

    status: Optional[str] = None


class DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str

    type: Literal["input_text"]


class DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]

    type: Literal["input_image"]

    image_url: Optional[str] = None


DataInputOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        DataInputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputOpenAIResponseMessageContentUnionMember2(BaseModel):
    text: str

    type: Literal["output_text"]


class DataInputOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[DataInputOpenAIResponseMessageContentUnionMember1],
        List[DataInputOpenAIResponseMessageContentUnionMember2],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


DataInput: TypeAlias = Union[
    DataInputOpenAIResponseOutputMessageWebSearchToolCall,
    DataInputOpenAIResponseOutputMessageFunctionToolCall,
    DataInputOpenAIResponseInputFunctionToolCallOutput,
    DataInputOpenAIResponseMessage,
]


class DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str

    type: Literal["input_text"]


class DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]

    type: Literal["input_image"]

    image_url: Optional[str] = None


DataOutputOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        DataOutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class DataOutputOpenAIResponseMessageContentUnionMember2(BaseModel):
    text: str

    type: Literal["output_text"]


class DataOutputOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[DataOutputOpenAIResponseMessageContentUnionMember1],
        List[DataOutputOpenAIResponseMessageContentUnionMember2],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class DataOutputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Literal["web_search_call"]


class DataOutputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str

    call_id: str

    name: str

    type: Literal["function_call"]

    id: Optional[str] = None

    status: Optional[str] = None


class DataOutputOpenAIResponseOutputMessageMcpCall(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_call"]

    error: Optional[str] = None

    output: Optional[str] = None


class DataOutputOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]

    name: str

    description: Optional[str] = None


class DataOutputOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str

    server_label: str

    tools: List[DataOutputOpenAIResponseOutputMessageMcpListToolsTool]

    type: Literal["mcp_list_tools"]


DataOutput: TypeAlias = Annotated[
    Union[
        DataOutputOpenAIResponseMessage,
        DataOutputOpenAIResponseOutputMessageWebSearchToolCall,
        DataOutputOpenAIResponseOutputMessageFunctionToolCall,
        DataOutputOpenAIResponseOutputMessageMcpCall,
        DataOutputOpenAIResponseOutputMessageMcpListTools,
    ],
    PropertyInfo(discriminator="type"),
]


class DataError(BaseModel):
    code: str

    message: str


class Data(BaseModel):
    id: str

    created_at: int

    input: List[DataInput]

    model: str

    object: Literal["response"]

    output: List[DataOutput]

    parallel_tool_calls: bool

    status: str

    error: Optional[DataError] = None

    previous_response_id: Optional[str] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None

    truncation: Optional[str] = None

    user: Optional[str] = None


class ResponseListResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]

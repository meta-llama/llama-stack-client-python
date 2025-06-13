# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .response_object import ResponseObject

__all__ = [
    "ResponseObjectStream",
    "OpenAIResponseObjectStreamResponseCreated",
    "OpenAIResponseObjectStreamResponseOutputItemAdded",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItem",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools",
    "OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool",
    "OpenAIResponseObjectStreamResponseOutputItemDone",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItem",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools",
    "OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool",
    "OpenAIResponseObjectStreamResponseOutputTextDelta",
    "OpenAIResponseObjectStreamResponseOutputTextDone",
    "OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta",
    "OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone",
    "OpenAIResponseObjectStreamResponseWebSearchCallInProgress",
    "OpenAIResponseObjectStreamResponseWebSearchCallSearching",
    "OpenAIResponseObjectStreamResponseWebSearchCallCompleted",
    "OpenAIResponseObjectStreamResponseMcpListToolsInProgress",
    "OpenAIResponseObjectStreamResponseMcpListToolsFailed",
    "OpenAIResponseObjectStreamResponseMcpListToolsCompleted",
    "OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta",
    "OpenAIResponseObjectStreamResponseMcpCallArgumentsDone",
    "OpenAIResponseObjectStreamResponseMcpCallInProgress",
    "OpenAIResponseObjectStreamResponseMcpCallFailed",
    "OpenAIResponseObjectStreamResponseMcpCallCompleted",
    "OpenAIResponseObjectStreamResponseCompleted",
]


class OpenAIResponseObjectStreamResponseCreated(BaseModel):
    response: ResponseObject

    type: Literal["response.created"]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(
    BaseModel
):
    text: str

    type: Literal["input_text"]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(
    BaseModel
):
    detail: Literal["low", "high", "auto"]

    type: Literal["input_image"]

    image_url: Optional[str] = None


OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2(BaseModel):
    text: str

    type: Literal["output_text"]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember1],
        List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessageContentUnionMember2],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Literal["web_search_call"]


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str

    queries: List[str]

    status: str

    type: Literal["file_search_call"]

    results: Optional[List[Dict[str, Union[bool, float, str, List[object], object, None]]]] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str

    call_id: str

    name: str

    type: Literal["function_call"]

    id: Optional[str] = None

    status: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_call"]

    error: Optional[str] = None

    output: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]

    name: str

    description: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str

    server_label: str

    tools: List[OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListToolsTool]

    type: Literal["mcp_list_tools"]


OpenAIResponseObjectStreamResponseOutputItemAddedItem: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseMessage,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageWebSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFileSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageFunctionToolCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpCall,
        OpenAIResponseObjectStreamResponseOutputItemAddedItemOpenAIResponseOutputMessageMcpListTools,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemAdded(BaseModel):
    item: OpenAIResponseObjectStreamResponseOutputItemAddedItem
    """Corresponds to the various Message types in the Responses API.

    They are all under one type because the Responses API gives them all the same
    "type" value, and there is no way to tell them apart in certain scenarios.
    """

    output_index: int

    response_id: str

    sequence_number: int

    type: Literal["response.output_item.added"]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(
    BaseModel
):
    text: str

    type: Literal["input_text"]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(
    BaseModel
):
    detail: Literal["low", "high", "auto"]

    type: Literal["input_image"]

    image_url: Optional[str] = None


OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2(BaseModel):
    text: str

    type: Literal["output_text"]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage(BaseModel):
    content: Union[
        str,
        List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember1],
        List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessageContentUnionMember2],
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Literal["web_search_call"]


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall(BaseModel):
    id: str

    queries: List[str]

    status: str

    type: Literal["file_search_call"]

    results: Optional[List[Dict[str, Union[bool, float, str, List[object], object, None]]]] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    arguments: str

    call_id: str

    name: str

    type: Literal["function_call"]

    id: Optional[str] = None

    status: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall(BaseModel):
    id: str

    arguments: str

    name: str

    server_label: str

    type: Literal["mcp_call"]

    error: Optional[str] = None

    output: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool(BaseModel):
    input_schema: Dict[str, Union[bool, float, str, List[object], object, None]]

    name: str

    description: Optional[str] = None


class OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools(BaseModel):
    id: str

    server_label: str

    tools: List[OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListToolsTool]

    type: Literal["mcp_list_tools"]


OpenAIResponseObjectStreamResponseOutputItemDoneItem: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseMessage,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageWebSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFileSearchToolCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageFunctionToolCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpCall,
        OpenAIResponseObjectStreamResponseOutputItemDoneItemOpenAIResponseOutputMessageMcpListTools,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIResponseObjectStreamResponseOutputItemDone(BaseModel):
    item: OpenAIResponseObjectStreamResponseOutputItemDoneItem
    """Corresponds to the various Message types in the Responses API.

    They are all under one type because the Responses API gives them all the same
    "type" value, and there is no way to tell them apart in certain scenarios.
    """

    output_index: int

    response_id: str

    sequence_number: int

    type: Literal["response.output_item.done"]


class OpenAIResponseObjectStreamResponseOutputTextDelta(BaseModel):
    content_index: int

    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.output_text.delta"]


class OpenAIResponseObjectStreamResponseOutputTextDone(BaseModel):
    content_index: int

    item_id: str

    output_index: int

    sequence_number: int

    text: str

    type: Literal["response.output_text.done"]


class OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta(BaseModel):
    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.function_call_arguments.delta"]


class OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone(BaseModel):
    arguments: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.function_call_arguments.done"]


class OpenAIResponseObjectStreamResponseWebSearchCallInProgress(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.web_search_call.in_progress"]


class OpenAIResponseObjectStreamResponseWebSearchCallSearching(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.web_search_call.searching"]


class OpenAIResponseObjectStreamResponseWebSearchCallCompleted(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.web_search_call.completed"]


class OpenAIResponseObjectStreamResponseMcpListToolsInProgress(BaseModel):
    sequence_number: int

    type: Literal["response.mcp_list_tools.in_progress"]


class OpenAIResponseObjectStreamResponseMcpListToolsFailed(BaseModel):
    sequence_number: int

    type: Literal["response.mcp_list_tools.failed"]


class OpenAIResponseObjectStreamResponseMcpListToolsCompleted(BaseModel):
    sequence_number: int

    type: Literal["response.mcp_list_tools.completed"]


class OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta(BaseModel):
    delta: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.mcp_call.arguments.delta"]


class OpenAIResponseObjectStreamResponseMcpCallArgumentsDone(BaseModel):
    arguments: str

    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.mcp_call.arguments.done"]


class OpenAIResponseObjectStreamResponseMcpCallInProgress(BaseModel):
    item_id: str

    output_index: int

    sequence_number: int

    type: Literal["response.mcp_call.in_progress"]


class OpenAIResponseObjectStreamResponseMcpCallFailed(BaseModel):
    sequence_number: int

    type: Literal["response.mcp_call.failed"]


class OpenAIResponseObjectStreamResponseMcpCallCompleted(BaseModel):
    sequence_number: int

    type: Literal["response.mcp_call.completed"]


class OpenAIResponseObjectStreamResponseCompleted(BaseModel):
    response: ResponseObject

    type: Literal["response.completed"]


ResponseObjectStream: TypeAlias = Annotated[
    Union[
        OpenAIResponseObjectStreamResponseCreated,
        OpenAIResponseObjectStreamResponseOutputItemAdded,
        OpenAIResponseObjectStreamResponseOutputItemDone,
        OpenAIResponseObjectStreamResponseOutputTextDelta,
        OpenAIResponseObjectStreamResponseOutputTextDone,
        OpenAIResponseObjectStreamResponseFunctionCallArgumentsDelta,
        OpenAIResponseObjectStreamResponseFunctionCallArgumentsDone,
        OpenAIResponseObjectStreamResponseWebSearchCallInProgress,
        OpenAIResponseObjectStreamResponseWebSearchCallSearching,
        OpenAIResponseObjectStreamResponseWebSearchCallCompleted,
        OpenAIResponseObjectStreamResponseMcpListToolsInProgress,
        OpenAIResponseObjectStreamResponseMcpListToolsFailed,
        OpenAIResponseObjectStreamResponseMcpListToolsCompleted,
        OpenAIResponseObjectStreamResponseMcpCallArgumentsDelta,
        OpenAIResponseObjectStreamResponseMcpCallArgumentsDone,
        OpenAIResponseObjectStreamResponseMcpCallInProgress,
        OpenAIResponseObjectStreamResponseMcpCallFailed,
        OpenAIResponseObjectStreamResponseMcpCallCompleted,
        OpenAIResponseObjectStreamResponseCompleted,
    ],
    PropertyInfo(discriminator="type"),
]

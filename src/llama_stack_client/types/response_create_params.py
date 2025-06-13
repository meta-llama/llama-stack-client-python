# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ResponseCreateParamsBase",
    "InputUnionMember1",
    "InputUnionMember1OpenAIResponseOutputMessageWebSearchToolCall",
    "InputUnionMember1OpenAIResponseOutputMessageFileSearchToolCall",
    "InputUnionMember1OpenAIResponseOutputMessageFunctionToolCall",
    "InputUnionMember1OpenAIResponseInputFunctionToolCallOutput",
    "InputUnionMember1OpenAIResponseMessage",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember1",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "InputUnionMember1OpenAIResponseMessageContentUnionMember2",
    "Text",
    "TextFormat",
    "Tool",
    "ToolOpenAIResponseInputToolWebSearch",
    "ToolOpenAIResponseInputToolFileSearch",
    "ToolOpenAIResponseInputToolFileSearchRankingOptions",
    "ToolOpenAIResponseInputToolFunction",
    "ToolOpenAIResponseInputToolMcp",
    "ToolOpenAIResponseInputToolMcpRequireApproval",
    "ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter",
    "ToolOpenAIResponseInputToolMcpAllowedTools",
    "ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter",
    "ResponseCreateParamsNonStreaming",
    "ResponseCreateParamsStreaming",
]


class ResponseCreateParamsBase(TypedDict, total=False):
    input: Required[Union[str, Iterable[InputUnionMember1]]]
    """Input message(s) to create the response."""

    model: Required[str]
    """The underlying LLM used for completions."""

    instructions: str

    max_infer_iters: int

    previous_response_id: str
    """
    (Optional) if specified, the new response will be a continuation of the previous
    response. This can be used to easily fork-off new responses from existing
    responses.
    """

    store: bool

    temperature: float

    text: Text

    tools: Iterable[Tool]


class InputUnionMember1OpenAIResponseOutputMessageWebSearchToolCall(TypedDict, total=False):
    id: Required[str]

    status: Required[str]

    type: Required[Literal["web_search_call"]]


class InputUnionMember1OpenAIResponseOutputMessageFileSearchToolCall(TypedDict, total=False):
    id: Required[str]

    queries: Required[List[str]]

    status: Required[str]

    type: Required[Literal["file_search_call"]]

    results: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]


class InputUnionMember1OpenAIResponseOutputMessageFunctionToolCall(TypedDict, total=False):
    arguments: Required[str]

    call_id: Required[str]

    name: Required[str]

    type: Required[Literal["function_call"]]

    id: str

    status: str


class InputUnionMember1OpenAIResponseInputFunctionToolCallOutput(TypedDict, total=False):
    call_id: Required[str]

    output: Required[str]

    type: Required[Literal["function_call_output"]]

    id: str

    status: str


class InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(
    TypedDict, total=False
):
    text: Required[str]

    type: Required[Literal["input_text"]]


class InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(
    TypedDict, total=False
):
    detail: Required[Literal["low", "high", "auto"]]

    type: Required[Literal["input_image"]]

    image_url: str


InputUnionMember1OpenAIResponseMessageContentUnionMember1: TypeAlias = Union[
    InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
    InputUnionMember1OpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
]


class InputUnionMember1OpenAIResponseMessageContentUnionMember2(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["output_text"]]


class InputUnionMember1OpenAIResponseMessage(TypedDict, total=False):
    content: Required[
        Union[
            str,
            Iterable[InputUnionMember1OpenAIResponseMessageContentUnionMember1],
            Iterable[InputUnionMember1OpenAIResponseMessageContentUnionMember2],
        ]
    ]

    role: Required[Literal["system", "developer", "user", "assistant"]]

    type: Required[Literal["message"]]

    id: str

    status: str


InputUnionMember1: TypeAlias = Union[
    InputUnionMember1OpenAIResponseOutputMessageWebSearchToolCall,
    InputUnionMember1OpenAIResponseOutputMessageFileSearchToolCall,
    InputUnionMember1OpenAIResponseOutputMessageFunctionToolCall,
    InputUnionMember1OpenAIResponseInputFunctionToolCallOutput,
    InputUnionMember1OpenAIResponseMessage,
]


class TextFormat(TypedDict, total=False):
    type: Required[Literal["text", "json_schema", "json_object"]]
    """Must be "text", "json_schema", or "json_object" to identify the format type"""

    description: str
    """(Optional) A description of the response format. Only used for json_schema."""

    name: str
    """The name of the response format. Only used for json_schema."""

    schema: Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    """The JSON schema the response should conform to.

    In a Python SDK, this is often a `pydantic` model. Only used for json_schema.
    """

    strict: bool
    """(Optional) Whether to strictly enforce the JSON schema.

    If true, the response must match the schema exactly. Only used for json_schema.
    """


class Text(TypedDict, total=False):
    format: TextFormat
    """Configuration for Responses API text format."""


class ToolOpenAIResponseInputToolWebSearch(TypedDict, total=False):
    type: Required[Literal["web_search", "web_search_preview_2025_03_11"]]

    search_context_size: str


class ToolOpenAIResponseInputToolFileSearchRankingOptions(TypedDict, total=False):
    ranker: str

    score_threshold: float


class ToolOpenAIResponseInputToolFileSearch(TypedDict, total=False):
    type: Required[Literal["file_search"]]

    vector_store_ids: Required[List[str]]

    filters: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    max_num_results: int

    ranking_options: ToolOpenAIResponseInputToolFileSearchRankingOptions


class ToolOpenAIResponseInputToolFunction(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["function"]]

    description: str

    parameters: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    strict: bool


class ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter(TypedDict, total=False):
    always: List[str]

    never: List[str]


ToolOpenAIResponseInputToolMcpRequireApproval: TypeAlias = Union[
    Literal["always", "never"], ToolOpenAIResponseInputToolMcpRequireApprovalApprovalFilter
]


class ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter(TypedDict, total=False):
    tool_names: List[str]


ToolOpenAIResponseInputToolMcpAllowedTools: TypeAlias = Union[
    List[str], ToolOpenAIResponseInputToolMcpAllowedToolsAllowedToolsFilter
]


class ToolOpenAIResponseInputToolMcp(TypedDict, total=False):
    require_approval: Required[ToolOpenAIResponseInputToolMcpRequireApproval]

    server_label: Required[str]

    server_url: Required[str]

    type: Required[Literal["mcp"]]

    allowed_tools: ToolOpenAIResponseInputToolMcpAllowedTools

    headers: Dict[str, Union[bool, float, str, Iterable[object], object, None]]


Tool: TypeAlias = Union[
    ToolOpenAIResponseInputToolWebSearch,
    ToolOpenAIResponseInputToolFileSearch,
    ToolOpenAIResponseInputToolFunction,
    ToolOpenAIResponseInputToolMcp,
]


class ResponseCreateParamsNonStreaming(ResponseCreateParamsBase, total=False):
    stream: Literal[False]


class ResponseCreateParamsStreaming(ResponseCreateParamsBase):
    stream: Required[Literal[True]]


ResponseCreateParams = Union[ResponseCreateParamsNonStreaming, ResponseCreateParamsStreaming]

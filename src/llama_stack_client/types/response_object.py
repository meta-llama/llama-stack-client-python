# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResponseObject",
    "Output",
    "OutputOpenAIResponseOutputMessage",
    "OutputOpenAIResponseOutputMessageContent",
    "OutputOpenAIResponseOutputMessageWebSearchToolCall",
    "Error",
]


class OutputOpenAIResponseOutputMessageContent(BaseModel):
    text: str

    type: Literal["output_text"]


class OutputOpenAIResponseOutputMessage(BaseModel):
    id: str

    content: List[OutputOpenAIResponseOutputMessageContent]

    role: Literal["assistant"]

    status: str

    type: Literal["message"]


class OutputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Literal["web_search_call"]


Output: TypeAlias = Annotated[
    Union[OutputOpenAIResponseOutputMessage, OutputOpenAIResponseOutputMessageWebSearchToolCall],
    PropertyInfo(discriminator="type"),
]


class Error(BaseModel):
    code: str

    message: str


class ResponseObject(BaseModel):
    id: str

    created_at: int

    model: str

    object: Literal["response"]

    output: List[Output]

    parallel_tool_calls: bool

    status: str

    error: Optional[Error] = None

    previous_response_id: Optional[str] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = None

    truncation: Optional[str] = None

    user: Optional[str] = None

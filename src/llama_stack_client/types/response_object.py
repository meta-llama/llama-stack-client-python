# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "ResponseObject",
    "Output",
    "OutputOpenAIResponseMessage",
    "OutputOpenAIResponseMessageContentUnionMember1",
    "OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText",
    "OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage",
    "OutputOpenAIResponseMessageContentUnionMember2",
    "OutputOpenAIResponseOutputMessageWebSearchToolCall",
    "OutputOpenAIResponseOutputMessageFunctionToolCall",
    "Error",
]


class OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText(BaseModel):
    text: str

    type: Literal["input_text"]


class OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage(BaseModel):
    detail: Literal["low", "high", "auto"]

    type: Literal["input_image"]

    image_url: Optional[str] = None


OutputOpenAIResponseMessageContentUnionMember1: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentText,
        OutputOpenAIResponseMessageContentUnionMember1OpenAIResponseInputMessageContentImage,
    ],
    PropertyInfo(discriminator="type"),
]


class OutputOpenAIResponseMessageContentUnionMember2(BaseModel):
    text: str

    type: Literal["output_text"]


class OutputOpenAIResponseMessage(BaseModel):
    content: Union[
        str, List[OutputOpenAIResponseMessageContentUnionMember1], List[OutputOpenAIResponseMessageContentUnionMember2]
    ]

    role: Literal["system", "developer", "user", "assistant"]

    type: Literal["message"]

    id: Optional[str] = None

    status: Optional[str] = None


class OutputOpenAIResponseOutputMessageWebSearchToolCall(BaseModel):
    id: str

    status: str

    type: Literal["web_search_call"]


class OutputOpenAIResponseOutputMessageFunctionToolCall(BaseModel):
    id: str

    arguments: str

    call_id: str

    name: str

    status: str

    type: Literal["function_call"]


Output: TypeAlias = Annotated[
    Union[
        OutputOpenAIResponseMessage,
        OutputOpenAIResponseOutputMessageWebSearchToolCall,
        OutputOpenAIResponseOutputMessageFunctionToolCall,
    ],
    PropertyInfo(discriminator="type"),
]


class Error(BaseModel):
    code: str

    message: str


class ResponseObject(BaseModel):
    @property
    def output_text(self) -> str:
        texts: List[str] = []
        for output in self.output:
            if output.type == "message":
                for content in output.content:
                    if content.type == "output_text":
                        texts.append(content.text)
        return "".join(texts)

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

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "CompletionListResponse",
    "Data",
    "DataChoice",
    "DataChoiceMessage",
    "DataChoiceMessageOpenAIUserMessageParam",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataChoiceMessageOpenAISystemMessageParam",
    "DataChoiceMessageOpenAISystemMessageParamContentUnionMember1",
    "DataChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataChoiceMessageOpenAIAssistantMessageParam",
    "DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1",
    "DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataChoiceMessageOpenAIAssistantMessageParamToolCall",
    "DataChoiceMessageOpenAIAssistantMessageParamToolCallFunction",
    "DataChoiceMessageOpenAIToolMessageParam",
    "DataChoiceMessageOpenAIToolMessageParamContentUnionMember1",
    "DataChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataChoiceMessageOpenAIDeveloperMessageParam",
    "DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1",
    "DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataChoiceLogprobs",
    "DataChoiceLogprobsContent",
    "DataChoiceLogprobsContentTopLogprob",
    "DataChoiceLogprobsRefusal",
    "DataChoiceLogprobsRefusalTopLogprob",
    "DataInputMessage",
    "DataInputMessageOpenAIUserMessageParam",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataInputMessageOpenAISystemMessageParam",
    "DataInputMessageOpenAISystemMessageParamContentUnionMember1",
    "DataInputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataInputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataInputMessageOpenAIAssistantMessageParam",
    "DataInputMessageOpenAIAssistantMessageParamContentUnionMember1",
    "DataInputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataInputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataInputMessageOpenAIAssistantMessageParamToolCall",
    "DataInputMessageOpenAIAssistantMessageParamToolCallFunction",
    "DataInputMessageOpenAIToolMessageParam",
    "DataInputMessageOpenAIToolMessageParamContentUnionMember1",
    "DataInputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataInputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "DataInputMessageOpenAIDeveloperMessageParam",
    "DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1",
    "DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
]


class DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataChoiceMessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataChoiceMessageOpenAIUserMessageParam(BaseModel):
    content: Union[str, List[DataChoiceMessageOpenAIUserMessageParamContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class DataChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class DataChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        DataChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataChoiceMessageOpenAISystemMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataChoiceMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[DataChoiceMessageOpenAISystemMessageParamContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Literal["text"]


class DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    image_url: (
        DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataChoiceMessageOpenAIAssistantMessageParamToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class DataChoiceMessageOpenAIAssistantMessageParamToolCall(BaseModel):
    type: Literal["function"]

    id: Optional[str] = None

    function: Optional[DataChoiceMessageOpenAIAssistantMessageParamToolCallFunction] = None

    index: Optional[int] = None


class DataChoiceMessageOpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[DataChoiceMessageOpenAIAssistantMessageParamContentUnionMember1], None] = None
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[DataChoiceMessageOpenAIAssistantMessageParamToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class DataChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class DataChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        DataChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataChoiceMessageOpenAIToolMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataChoiceMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[DataChoiceMessageOpenAIToolMessageParamContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(
    BaseModel
):
    text: str

    type: Literal["text"]


class DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    image_url: (
        DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[DataChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


DataChoiceMessage: TypeAlias = Annotated[
    Union[
        DataChoiceMessageOpenAIUserMessageParam,
        DataChoiceMessageOpenAISystemMessageParam,
        DataChoiceMessageOpenAIAssistantMessageParam,
        DataChoiceMessageOpenAIToolMessageParam,
        DataChoiceMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class DataChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class DataChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[DataChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class DataChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class DataChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[DataChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class DataChoiceLogprobs(BaseModel):
    content: Optional[List[DataChoiceLogprobsContent]] = None
    """(Optional) The log probabilities for the tokens in the message"""

    refusal: Optional[List[DataChoiceLogprobsRefusal]] = None
    """(Optional) The log probabilities for the tokens in the message"""


class DataChoice(BaseModel):
    finish_reason: str
    """The reason the model stopped generating"""

    index: int
    """The index of the choice"""

    message: DataChoiceMessage
    """The message from the model"""

    logprobs: Optional[DataChoiceLogprobs] = None
    """(Optional) The log probabilities for the tokens in the message"""


class DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataInputMessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataInputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputMessageOpenAIUserMessageParam(BaseModel):
    content: Union[str, List[DataInputMessageOpenAIUserMessageParamContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class DataInputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class DataInputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataInputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        DataInputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataInputMessageOpenAISystemMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataInputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[DataInputMessageOpenAISystemMessageParamContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class DataInputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class DataInputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataInputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    image_url: (
        DataInputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataInputMessageOpenAIAssistantMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataInputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputMessageOpenAIAssistantMessageParamToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class DataInputMessageOpenAIAssistantMessageParamToolCall(BaseModel):
    type: Literal["function"]

    id: Optional[str] = None

    function: Optional[DataInputMessageOpenAIAssistantMessageParamToolCallFunction] = None

    index: Optional[int] = None


class DataInputMessageOpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[DataInputMessageOpenAIAssistantMessageParamContentUnionMember1], None] = None
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[DataInputMessageOpenAIAssistantMessageParamToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class DataInputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class DataInputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataInputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        DataInputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataInputMessageOpenAIToolMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataInputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[DataInputMessageOpenAIToolMessageParamContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(
    BaseModel
):
    image_url: (
        DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class DataInputMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[DataInputMessageOpenAIDeveloperMessageParamContentUnionMember1]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


DataInputMessage: TypeAlias = Annotated[
    Union[
        DataInputMessageOpenAIUserMessageParam,
        DataInputMessageOpenAISystemMessageParam,
        DataInputMessageOpenAIAssistantMessageParam,
        DataInputMessageOpenAIToolMessageParam,
        DataInputMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class Data(BaseModel):
    id: str
    """The ID of the chat completion"""

    choices: List[DataChoice]
    """List of choices"""

    created: int
    """The Unix timestamp in seconds when the chat completion was created"""

    input_messages: List[DataInputMessage]

    model: str
    """The model that was used to generate the chat completion"""

    object: Literal["chat.completion"]
    """The object type, which will be "chat.completion" """


class CompletionListResponse(BaseModel):
    data: List[Data]

    first_id: str

    has_more: bool

    last_id: str

    object: Literal["list"]

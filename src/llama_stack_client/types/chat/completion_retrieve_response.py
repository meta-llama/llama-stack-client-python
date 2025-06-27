# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "CompletionRetrieveResponse",
    "Choice",
    "ChoiceMessage",
    "ChoiceMessageOpenAIUserMessageParam",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "ChoiceMessageOpenAISystemMessageParam",
    "ChoiceMessageOpenAISystemMessageParamContentUnionMember1",
    "ChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "ChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "ChoiceMessageOpenAIAssistantMessageParam",
    "ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1",
    "ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "ChoiceMessageOpenAIAssistantMessageParamToolCall",
    "ChoiceMessageOpenAIAssistantMessageParamToolCallFunction",
    "ChoiceMessageOpenAIToolMessageParam",
    "ChoiceMessageOpenAIToolMessageParamContentUnionMember1",
    "ChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "ChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "ChoiceMessageOpenAIDeveloperMessageParam",
    "ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1",
    "ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprob",
    "ChoiceLogprobsRefusal",
    "ChoiceLogprobsRefusalTopLogprob",
    "InputMessage",
    "InputMessageOpenAIUserMessageParam",
    "InputMessageOpenAIUserMessageParamContentUnionMember1",
    "InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "InputMessageOpenAISystemMessageParam",
    "InputMessageOpenAISystemMessageParamContentUnionMember1",
    "InputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "InputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "InputMessageOpenAIAssistantMessageParam",
    "InputMessageOpenAIAssistantMessageParamContentUnionMember1",
    "InputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "InputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "InputMessageOpenAIAssistantMessageParamToolCall",
    "InputMessageOpenAIAssistantMessageParamToolCallFunction",
    "InputMessageOpenAIToolMessageParam",
    "InputMessageOpenAIToolMessageParamContentUnionMember1",
    "InputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "InputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
    "InputMessageOpenAIDeveloperMessageParam",
    "InputMessageOpenAIDeveloperMessageParamContentUnionMember1",
    "InputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam",
    "InputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam",
    "InputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL",
]


class ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


ChoiceMessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        ChoiceMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class ChoiceMessageOpenAIUserMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAIUserMessageParamContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class ChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class ChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class ChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: ChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


ChoiceMessageOpenAISystemMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        ChoiceMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class ChoiceMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAISystemMessageParamContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class ChoiceMessageOpenAIAssistantMessageParamToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class ChoiceMessageOpenAIAssistantMessageParamToolCall(BaseModel):
    type: Literal["function"]

    id: Optional[str] = None

    function: Optional[ChoiceMessageOpenAIAssistantMessageParamToolCallFunction] = None

    index: Optional[int] = None


class ChoiceMessageOpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[ChoiceMessageOpenAIAssistantMessageParamContentUnionMember1], None] = None
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[ChoiceMessageOpenAIAssistantMessageParamToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class ChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class ChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class ChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: ChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


ChoiceMessageOpenAIToolMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        ChoiceMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class ChoiceMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAIToolMessageParamContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class ChoiceMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[ChoiceMessageOpenAIDeveloperMessageParamContentUnionMember1]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


ChoiceMessage: TypeAlias = Annotated[
    Union[
        ChoiceMessageOpenAIUserMessageParam,
        ChoiceMessageOpenAISystemMessageParam,
        ChoiceMessageOpenAIAssistantMessageParam,
        ChoiceMessageOpenAIToolMessageParam,
        ChoiceMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class ChoiceLogprobsContentTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsContent(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceLogprobsContentTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceLogprobsRefusalTopLogprob(BaseModel):
    token: str

    logprob: float

    bytes: Optional[List[int]] = None


class ChoiceLogprobsRefusal(BaseModel):
    token: str

    logprob: float

    top_logprobs: List[ChoiceLogprobsRefusalTopLogprob]

    bytes: Optional[List[int]] = None


class ChoiceLogprobs(BaseModel):
    content: Optional[List[ChoiceLogprobsContent]] = None
    """(Optional) The log probabilities for the tokens in the message"""

    refusal: Optional[List[ChoiceLogprobsRefusal]] = None
    """(Optional) The log probabilities for the tokens in the message"""


class Choice(BaseModel):
    finish_reason: str
    """The reason the model stopped generating"""

    index: int
    """The index of the choice"""

    message: ChoiceMessage
    """The message from the model"""

    logprobs: Optional[ChoiceLogprobs] = None
    """(Optional) The log probabilities for the tokens in the message"""


class InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(BaseModel):
    url: str

    detail: Optional[str] = None


class InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


InputMessageOpenAIUserMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        InputMessageOpenAIUserMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class InputMessageOpenAIUserMessageParam(BaseModel):
    content: Union[str, List[InputMessageOpenAIUserMessageParamContentUnionMember1]]
    """The content of the message, which can include text and other media"""

    role: Literal["user"]
    """Must be "user" to identify this as a user message"""

    name: Optional[str] = None
    """(Optional) The name of the user message participant."""


class InputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class InputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class InputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: InputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


InputMessageOpenAISystemMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        InputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        InputMessageOpenAISystemMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class InputMessageOpenAISystemMessageParam(BaseModel):
    content: Union[str, List[InputMessageOpenAISystemMessageParamContentUnionMember1]]
    """The content of the "system prompt".

    If multiple system messages are provided, they are concatenated. The underlying
    Llama Stack code may also add other system messages (for example, for formatting
    tool definitions).
    """

    role: Literal["system"]
    """Must be "system" to identify this as a system message"""

    name: Optional[str] = None
    """(Optional) The name of the system message participant."""


class InputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class InputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class InputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        InputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


InputMessageOpenAIAssistantMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        InputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        InputMessageOpenAIAssistantMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class InputMessageOpenAIAssistantMessageParamToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class InputMessageOpenAIAssistantMessageParamToolCall(BaseModel):
    type: Literal["function"]

    id: Optional[str] = None

    function: Optional[InputMessageOpenAIAssistantMessageParamToolCallFunction] = None

    index: Optional[int] = None


class InputMessageOpenAIAssistantMessageParam(BaseModel):
    role: Literal["assistant"]
    """Must be "assistant" to identify this as the model's response"""

    content: Union[str, List[InputMessageOpenAIAssistantMessageParamContentUnionMember1], None] = None
    """The content of the model's response"""

    name: Optional[str] = None
    """(Optional) The name of the assistant message participant."""

    tool_calls: Optional[List[InputMessageOpenAIAssistantMessageParamToolCall]] = None
    """List of tool calls. Each tool call is an OpenAIChatCompletionToolCall object."""


class InputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class InputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(BaseModel):
    url: str

    detail: Optional[str] = None


class InputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: InputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL

    type: Literal["image_url"]


InputMessageOpenAIToolMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        InputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        InputMessageOpenAIToolMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class InputMessageOpenAIToolMessageParam(BaseModel):
    content: Union[str, List[InputMessageOpenAIToolMessageParamContentUnionMember1]]
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

    tool_call_id: str
    """Unique identifier for the tool call this response is for"""


class InputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam(BaseModel):
    text: str

    type: Literal["text"]


class InputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL(
    BaseModel
):
    url: str

    detail: Optional[str] = None


class InputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam(BaseModel):
    image_url: (
        InputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParamImageURL
    )

    type: Literal["image_url"]


InputMessageOpenAIDeveloperMessageParamContentUnionMember1: TypeAlias = Annotated[
    Union[
        InputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartTextParam,
        InputMessageOpenAIDeveloperMessageParamContentUnionMember1OpenAIChatCompletionContentPartImageParam,
    ],
    PropertyInfo(discriminator="type"),
]


class InputMessageOpenAIDeveloperMessageParam(BaseModel):
    content: Union[str, List[InputMessageOpenAIDeveloperMessageParamContentUnionMember1]]
    """The content of the developer message"""

    role: Literal["developer"]
    """Must be "developer" to identify this as a developer message"""

    name: Optional[str] = None
    """(Optional) The name of the developer message participant."""


InputMessage: TypeAlias = Annotated[
    Union[
        InputMessageOpenAIUserMessageParam,
        InputMessageOpenAISystemMessageParam,
        InputMessageOpenAIAssistantMessageParam,
        InputMessageOpenAIToolMessageParam,
        InputMessageOpenAIDeveloperMessageParam,
    ],
    PropertyInfo(discriminator="role"),
]


class CompletionRetrieveResponse(BaseModel):
    id: str
    """The ID of the chat completion"""

    choices: List[Choice]
    """List of choices"""

    created: int
    """The Unix timestamp in seconds when the chat completion was created"""

    input_messages: List[InputMessage]

    model: str
    """The model that was used to generate the chat completion"""

    object: Literal["chat.completion"]
    """The object type, which will be "chat.completion" """

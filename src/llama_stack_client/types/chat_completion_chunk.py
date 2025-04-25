# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ChatCompletionChunk",
    "Choice",
    "ChoiceDelta",
    "ChoiceDeltaToolCall",
    "ChoiceDeltaToolCallFunction",
    "ChoiceLogprobs",
    "ChoiceLogprobsContent",
    "ChoiceLogprobsContentTopLogprob",
    "ChoiceLogprobsRefusal",
    "ChoiceLogprobsRefusalTopLogprob",
]


class ChoiceDeltaToolCallFunction(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class ChoiceDeltaToolCall(BaseModel):
    type: Literal["function"]

    id: Optional[str] = None

    function: Optional[ChoiceDeltaToolCallFunction] = None

    index: Optional[int] = None


class ChoiceDelta(BaseModel):
    content: Optional[str] = None
    """(Optional) The content of the delta"""

    refusal: Optional[str] = None
    """(Optional) The refusal of the delta"""

    role: Optional[str] = None
    """(Optional) The role of the delta"""

    tool_calls: Optional[List[ChoiceDeltaToolCall]] = None
    """(Optional) The tool calls of the delta"""


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
    delta: ChoiceDelta
    """The delta from the chunk"""

    finish_reason: str
    """The reason the model stopped generating"""

    index: int
    """The index of the choice"""

    logprobs: Optional[ChoiceLogprobs] = None
    """(Optional) The log probabilities for the tokens in the message"""


class ChatCompletionChunk(BaseModel):
    id: str
    """The ID of the chat completion"""

    choices: List[Choice]
    """List of choices"""

    created: int
    """The Unix timestamp in seconds when the chat completion was created"""

    model: str
    """The model that was used to generate the chat completion"""

    object: Literal["chat.completion.chunk"]
    """The object type, which will be "chat.completion.chunk" """

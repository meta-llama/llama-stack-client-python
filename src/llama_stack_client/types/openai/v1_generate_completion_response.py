# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .choice_logprobs import ChoiceLogprobs

__all__ = ["V1GenerateCompletionResponse", "Choice"]


class Choice(BaseModel):
    finish_reason: str

    index: int

    text: str

    logprobs: Optional[ChoiceLogprobs] = None
    """
    The log probabilities for the tokens in the message from an OpenAI-compatible
    chat completion response.
    """


class V1GenerateCompletionResponse(BaseModel):
    id: str

    choices: List[Choice]

    created: int

    model: str

    object: Literal["text_completion"]

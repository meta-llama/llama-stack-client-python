# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.user_message import UserMessage
from .shared.system_message import SystemMessage
from .shared.completion_message import CompletionMessage
from .shared.tool_response_message import ToolResponseMessage

__all__ = ["ScoredDialogGenerations", "Dialog", "ScoredGeneration", "ScoredGenerationMessage"]

Dialog: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]

ScoredGenerationMessage: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]


class ScoredGeneration(BaseModel):
    message: ScoredGenerationMessage

    score: float


class ScoredDialogGenerations(BaseModel):
    dialog: List[Dialog]

    scored_generations: List[ScoredGeneration]

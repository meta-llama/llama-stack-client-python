# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.user_message import UserMessage
from .shared.system_message import SystemMessage
from .shared.completion_message import CompletionMessage
from .shared.tool_response_message import ToolResponseMessage

__all__ = [
    "RewardScoringResponse",
    "ScoredGeneration",
    "ScoredGenerationDialog",
    "ScoredGenerationScoredGeneration",
    "ScoredGenerationScoredGenerationMessage",
]

ScoredGenerationDialog: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]

ScoredGenerationScoredGenerationMessage: TypeAlias = Union[
    UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage
]


class ScoredGenerationScoredGeneration(BaseModel):
    message: ScoredGenerationScoredGenerationMessage

    score: float


class ScoredGeneration(BaseModel):
    dialog: List[ScoredGenerationDialog]

    scored_generations: List[ScoredGenerationScoredGeneration]


class RewardScoringResponse(BaseModel):
    scored_generations: List[ScoredGeneration]

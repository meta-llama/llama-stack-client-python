# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel
from .shared.user_message import UserMessage
from .shared.system_message import SystemMessage
from .shared.completion_message import CompletionMessage
from .shared.tool_response_message import ToolResponseMessage

__all__ = [
    "SyntheticDataGenerationResponse",
    "SyntheticData",
    "SyntheticDataDialog",
    "SyntheticDataScoredGeneration",
    "SyntheticDataScoredGenerationMessage",
]

SyntheticDataDialog: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]

SyntheticDataScoredGenerationMessage: TypeAlias = Union[
    UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage
]


class SyntheticDataScoredGeneration(BaseModel):
    message: SyntheticDataScoredGenerationMessage

    score: float


class SyntheticData(BaseModel):
    dialog: List[SyntheticDataDialog]

    scored_generations: List[SyntheticDataScoredGeneration]


class SyntheticDataGenerationResponse(BaseModel):
    synthetic_data: List[SyntheticData]

    statistics: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

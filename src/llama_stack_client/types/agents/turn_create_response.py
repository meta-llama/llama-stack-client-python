# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .turn import Turn
from ..._models import BaseModel
from .turn_response_event import TurnResponseEvent

__all__ = ["TurnCreateResponse", "AgentTurnResponseStreamChunk"]


class AgentTurnResponseStreamChunk(BaseModel):
    event: TurnResponseEvent


TurnCreateResponse: TypeAlias = Union[Turn, AgentTurnResponseStreamChunk]

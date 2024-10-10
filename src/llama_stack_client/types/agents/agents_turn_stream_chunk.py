# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel
from .turn_stream_event import TurnStreamEvent

__all__ = ["AgentsTurnStreamChunk"]


class AgentsTurnStreamChunk(BaseModel):
    event: TurnStreamEvent

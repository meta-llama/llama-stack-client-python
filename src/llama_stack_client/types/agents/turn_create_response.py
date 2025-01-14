# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .turn import Turn
from ..._models import BaseModel
from ..inference_step import InferenceStep
from ..shield_call_step import ShieldCallStep
from ..tool_execution_step import ToolExecutionStep
from ..shared.content_delta import ContentDelta
from ..memory_retrieval_step import MemoryRetrievalStep

__all__ = [
    "TurnCreateResponse",
    "AgentTurnResponseStreamChunk",
    "AgentTurnResponseStreamChunkEvent",
    "AgentTurnResponseStreamChunkEventPayload",
    "AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepStartPayload",
    "AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepProgressPayload",
    "AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepCompletePayload",
    "AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepCompletePayloadStepDetails",
    "AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseTurnStartPayload",
    "AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseTurnCompletePayload",
]


class AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepStartPayload(BaseModel):
    event_type: Literal["step_start"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepProgressPayload(BaseModel):
    delta: ContentDelta

    event_type: Literal["step_progress"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]


AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepCompletePayloadStepDetails: TypeAlias = Union[
    InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep
]


class AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepCompletePayload(BaseModel):
    event_type: Literal["step_complete"]

    step_details: AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepCompletePayloadStepDetails

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]


class AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseTurnStartPayload(BaseModel):
    event_type: Literal["turn_start"]

    turn_id: str


class AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseTurnCompletePayload(BaseModel):
    event_type: Literal["turn_complete"]

    turn: Turn


AgentTurnResponseStreamChunkEventPayload: TypeAlias = Union[
    AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepStartPayload,
    AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepProgressPayload,
    AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseStepCompletePayload,
    AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseTurnStartPayload,
    AgentTurnResponseStreamChunkEventPayloadAgentTurnResponseTurnCompletePayload,
]


class AgentTurnResponseStreamChunkEvent(BaseModel):
    payload: AgentTurnResponseStreamChunkEventPayload


class AgentTurnResponseStreamChunk(BaseModel):
    event: AgentTurnResponseStreamChunkEvent


TurnCreateResponse: TypeAlias = Union[Turn, AgentTurnResponseStreamChunk]

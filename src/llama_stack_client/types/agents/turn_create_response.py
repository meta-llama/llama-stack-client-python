# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .turn import Turn
from ..._utils import PropertyInfo
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
    "AgentTurnResponseStreamChunkEventPayloadStepStart",
    "AgentTurnResponseStreamChunkEventPayloadStepProgress",
    "AgentTurnResponseStreamChunkEventPayloadStepComplete",
    "AgentTurnResponseStreamChunkEventPayloadStepCompleteStepDetails",
    "AgentTurnResponseStreamChunkEventPayloadTurnStart",
    "AgentTurnResponseStreamChunkEventPayloadTurnComplete",
]


class AgentTurnResponseStreamChunkEventPayloadStepStart(BaseModel):
    event_type: Literal["step_start"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class AgentTurnResponseStreamChunkEventPayloadStepProgress(BaseModel):
    delta: ContentDelta

    event_type: Literal["step_progress"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]


AgentTurnResponseStreamChunkEventPayloadStepCompleteStepDetails: TypeAlias = Annotated[
    Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep],
    PropertyInfo(discriminator="step_type"),
]


class AgentTurnResponseStreamChunkEventPayloadStepComplete(BaseModel):
    event_type: Literal["step_complete"]

    step_details: AgentTurnResponseStreamChunkEventPayloadStepCompleteStepDetails

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]


class AgentTurnResponseStreamChunkEventPayloadTurnStart(BaseModel):
    event_type: Literal["turn_start"]

    turn_id: str


class AgentTurnResponseStreamChunkEventPayloadTurnComplete(BaseModel):
    event_type: Literal["turn_complete"]

    turn: Turn


AgentTurnResponseStreamChunkEventPayload: TypeAlias = Annotated[
    Union[
        AgentTurnResponseStreamChunkEventPayloadStepStart,
        AgentTurnResponseStreamChunkEventPayloadStepProgress,
        AgentTurnResponseStreamChunkEventPayloadStepComplete,
        AgentTurnResponseStreamChunkEventPayloadTurnStart,
        AgentTurnResponseStreamChunkEventPayloadTurnComplete,
    ],
    PropertyInfo(discriminator="event_type"),
]


class AgentTurnResponseStreamChunkEvent(BaseModel):
    payload: AgentTurnResponseStreamChunkEventPayload


class AgentTurnResponseStreamChunk(BaseModel):
    event: AgentTurnResponseStreamChunkEvent


TurnCreateResponse: TypeAlias = Union[Turn, AgentTurnResponseStreamChunk]

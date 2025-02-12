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
    "TurnResponseEventPayload",
    "AgentTurnResponseStepStartPayload",
    "AgentTurnResponseStepProgressPayload",
    "AgentTurnResponseStepCompletePayload",
    "AgentTurnResponseStepCompletePayloadStepDetails",
    "AgentTurnResponseTurnStartPayload",
    "AgentTurnResponseTurnCompletePayload",
]


class AgentTurnResponseStepStartPayload(BaseModel):
    event_type: Literal["step_start"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class AgentTurnResponseStepProgressPayload(BaseModel):
    delta: ContentDelta

    event_type: Literal["step_progress"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]


AgentTurnResponseStepCompletePayloadStepDetails: TypeAlias = Annotated[
    Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep],
    PropertyInfo(discriminator="step_type"),
]


class AgentTurnResponseStepCompletePayload(BaseModel):
    event_type: Literal["step_complete"]

    step_details: AgentTurnResponseStepCompletePayloadStepDetails

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]


class AgentTurnResponseTurnStartPayload(BaseModel):
    event_type: Literal["turn_start"]

    turn_id: str


class AgentTurnResponseTurnCompletePayload(BaseModel):
    event_type: Literal["turn_complete"]

    turn: Turn
    """A single turn in an interaction with an Agentic System."""


TurnResponseEventPayload: TypeAlias = Annotated[
    Union[
        AgentTurnResponseStepStartPayload,
        AgentTurnResponseStepProgressPayload,
        AgentTurnResponseStepCompletePayload,
        AgentTurnResponseTurnStartPayload,
        AgentTurnResponseTurnCompletePayload,
    ],
    PropertyInfo(discriminator="event_type"),
]

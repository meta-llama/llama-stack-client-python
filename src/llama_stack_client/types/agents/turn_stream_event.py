# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .turn import Turn
from ..._models import BaseModel
from ..inference_step import InferenceStep
from ..shared.tool_call import ToolCall
from ..shield_call_step import ShieldCallStep
from ..tool_execution_step import ToolExecutionStep
from ..memory_retrieval_step import MemoryRetrievalStep

__all__ = [
    "TurnStreamEvent",
    "Payload",
    "PayloadAgentTurnResponseStepStartPayload",
    "PayloadAgentTurnResponseStepProgressPayload",
    "PayloadAgentTurnResponseStepProgressPayloadToolCallDelta",
    "PayloadAgentTurnResponseStepProgressPayloadToolCallDeltaContent",
    "PayloadAgentTurnResponseStepCompletePayload",
    "PayloadAgentTurnResponseStepCompletePayloadStepDetails",
    "PayloadAgentTurnResponseTurnStartPayload",
    "PayloadAgentTurnResponseTurnCompletePayload",
]


class PayloadAgentTurnResponseStepStartPayload(BaseModel):
    event_type: Literal["step_start"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


PayloadAgentTurnResponseStepProgressPayloadToolCallDeltaContent: TypeAlias = Union[str, ToolCall]


class PayloadAgentTurnResponseStepProgressPayloadToolCallDelta(BaseModel):
    content: PayloadAgentTurnResponseStepProgressPayloadToolCallDeltaContent

    parse_status: Literal["started", "in_progress", "failure", "success"]


class PayloadAgentTurnResponseStepProgressPayload(BaseModel):
    event_type: Literal["step_progress"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]

    text_delta_model_response: Optional[str] = FieldInfo(alias="model_response_text_delta", default=None)

    tool_call_delta: Optional[PayloadAgentTurnResponseStepProgressPayloadToolCallDelta] = None

    tool_response_text_delta: Optional[str] = None


PayloadAgentTurnResponseStepCompletePayloadStepDetails: TypeAlias = Union[
    InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep
]


class PayloadAgentTurnResponseStepCompletePayload(BaseModel):
    event_type: Literal["step_complete"]

    step_details: PayloadAgentTurnResponseStepCompletePayloadStepDetails

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]


class PayloadAgentTurnResponseTurnStartPayload(BaseModel):
    event_type: Literal["turn_start"]

    turn_id: str


class PayloadAgentTurnResponseTurnCompletePayload(BaseModel):
    event_type: Literal["turn_complete"]

    turn: Turn


Payload: TypeAlias = Union[
    PayloadAgentTurnResponseStepStartPayload,
    PayloadAgentTurnResponseStepProgressPayload,
    PayloadAgentTurnResponseStepCompletePayload,
    PayloadAgentTurnResponseTurnStartPayload,
    PayloadAgentTurnResponseTurnCompletePayload,
]


class TurnStreamEvent(BaseModel):
    payload: Payload

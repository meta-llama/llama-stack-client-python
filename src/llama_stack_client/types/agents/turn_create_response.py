# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .turn import Turn
from ..._models import BaseModel
from ..shared.tool_call import ToolCall
from ..shared.image_media import ImageMedia
from ..shared.completion_message import CompletionMessage

__all__ = [
    "TurnCreateResponse",
    "Event",
    "EventPayload",
    "EventPayloadAgentTurnResponseStepStartPayload",
    "EventPayloadAgentTurnResponseStepProgressPayload",
    "EventPayloadAgentTurnResponseStepProgressPayloadToolCallDelta",
    "EventPayloadAgentTurnResponseStepProgressPayloadToolCallDeltaContent",
    "EventPayloadAgentTurnResponseStepCompletePayload",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetails",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsInferenceStep",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStep",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStepToolResponse",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStepToolResponseContent",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStepToolResponseContentUnionMember2",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsShieldCallStep",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsShieldCallStepViolation",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsMemoryRetrievalStep",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsMemoryRetrievalStepInsertedContext",
    "EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsMemoryRetrievalStepInsertedContextUnionMember2",
    "EventPayloadAgentTurnResponseTurnStartPayload",
    "EventPayloadAgentTurnResponseTurnCompletePayload",
]


class EventPayloadAgentTurnResponseStepStartPayload(BaseModel):
    event_type: Literal["step_start"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


EventPayloadAgentTurnResponseStepProgressPayloadToolCallDeltaContent: TypeAlias = Union[str, ToolCall]


class EventPayloadAgentTurnResponseStepProgressPayloadToolCallDelta(BaseModel):
    content: EventPayloadAgentTurnResponseStepProgressPayloadToolCallDeltaContent

    parse_status: Literal["started", "in_progress", "failure", "success"]


class EventPayloadAgentTurnResponseStepProgressPayload(BaseModel):
    event_type: Literal["step_progress"]

    step_id: str

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]

    text_delta_model_response: Optional[str] = FieldInfo(alias="model_response_text_delta", default=None)

    tool_call_delta: Optional[EventPayloadAgentTurnResponseStepProgressPayloadToolCallDelta] = None

    tool_response_text_delta: Optional[str] = None


class EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsInferenceStep(BaseModel):
    inference_model_response: CompletionMessage = FieldInfo(alias="model_response")

    step_id: str

    step_type: Literal["inference"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None


EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStepToolResponseContentUnionMember2: TypeAlias = Union[
    str, ImageMedia
]

EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStepToolResponseContent: TypeAlias = Union[
    str,
    ImageMedia,
    List[EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStepToolResponseContentUnionMember2],
]


class EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStepToolResponse(BaseModel):
    call_id: str

    content: EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStepToolResponseContent

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]


class EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStep(BaseModel):
    step_id: str

    step_type: Literal["tool_execution"]

    tool_calls: List[ToolCall]

    tool_responses: List[EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStepToolResponse]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None


class EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsShieldCallStepViolation(BaseModel):
    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    violation_level: Literal["info", "warn", "error"]

    user_message: Optional[str] = None


class EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsShieldCallStep(BaseModel):
    step_id: str

    step_type: Literal["shield_call"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

    violation: Optional[EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsShieldCallStepViolation] = None


EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsMemoryRetrievalStepInsertedContextUnionMember2: TypeAlias = (
    Union[str, ImageMedia]
)

EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsMemoryRetrievalStepInsertedContext: TypeAlias = Union[
    str,
    ImageMedia,
    List[EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsMemoryRetrievalStepInsertedContextUnionMember2],
]


class EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsMemoryRetrievalStep(BaseModel):
    inserted_context: EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsMemoryRetrievalStepInsertedContext

    memory_bank_ids: List[str]

    step_id: str

    step_type: Literal["memory_retrieval"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None


EventPayloadAgentTurnResponseStepCompletePayloadStepDetails: TypeAlias = Union[
    EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsInferenceStep,
    EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsToolExecutionStep,
    EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsShieldCallStep,
    EventPayloadAgentTurnResponseStepCompletePayloadStepDetailsMemoryRetrievalStep,
]


class EventPayloadAgentTurnResponseStepCompletePayload(BaseModel):
    event_type: Literal["step_complete"]

    step_details: EventPayloadAgentTurnResponseStepCompletePayloadStepDetails

    step_type: Literal["inference", "tool_execution", "shield_call", "memory_retrieval"]


class EventPayloadAgentTurnResponseTurnStartPayload(BaseModel):
    event_type: Literal["turn_start"]

    turn_id: str


class EventPayloadAgentTurnResponseTurnCompletePayload(BaseModel):
    event_type: Literal["turn_complete"]

    turn: Turn


EventPayload: TypeAlias = Union[
    EventPayloadAgentTurnResponseStepStartPayload,
    EventPayloadAgentTurnResponseStepProgressPayload,
    EventPayloadAgentTurnResponseStepCompletePayload,
    EventPayloadAgentTurnResponseTurnStartPayload,
    EventPayloadAgentTurnResponseTurnCompletePayload,
]


class Event(BaseModel):
    payload: EventPayload


class TurnCreateResponse(BaseModel):
    event: Event

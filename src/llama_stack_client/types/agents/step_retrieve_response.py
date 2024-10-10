# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..shared.tool_call import ToolCall
from ..shared.image_media import ImageMedia
from ..shared.completion_message import CompletionMessage

__all__ = [
    "StepRetrieveResponse",
    "Step",
    "StepInferenceStep",
    "StepToolExecutionStep",
    "StepToolExecutionStepToolResponse",
    "StepToolExecutionStepToolResponseContent",
    "StepToolExecutionStepToolResponseContentUnionMember2",
    "StepShieldCallStep",
    "StepShieldCallStepViolation",
    "StepMemoryRetrievalStep",
    "StepMemoryRetrievalStepInsertedContext",
    "StepMemoryRetrievalStepInsertedContextUnionMember2",
]


class StepInferenceStep(BaseModel):
    inference_model_response: CompletionMessage = FieldInfo(alias="model_response")

    step_id: str

    step_type: Literal["inference"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None


StepToolExecutionStepToolResponseContentUnionMember2: TypeAlias = Union[str, ImageMedia]

StepToolExecutionStepToolResponseContent: TypeAlias = Union[
    str, ImageMedia, List[StepToolExecutionStepToolResponseContentUnionMember2]
]


class StepToolExecutionStepToolResponse(BaseModel):
    call_id: str

    content: StepToolExecutionStepToolResponseContent

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]


class StepToolExecutionStep(BaseModel):
    step_id: str

    step_type: Literal["tool_execution"]

    tool_calls: List[ToolCall]

    tool_responses: List[StepToolExecutionStepToolResponse]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None


class StepShieldCallStepViolation(BaseModel):
    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    violation_level: Literal["info", "warn", "error"]

    user_message: Optional[str] = None


class StepShieldCallStep(BaseModel):
    step_id: str

    step_type: Literal["shield_call"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

    violation: Optional[StepShieldCallStepViolation] = None


StepMemoryRetrievalStepInsertedContextUnionMember2: TypeAlias = Union[str, ImageMedia]

StepMemoryRetrievalStepInsertedContext: TypeAlias = Union[
    str, ImageMedia, List[StepMemoryRetrievalStepInsertedContextUnionMember2]
]


class StepMemoryRetrievalStep(BaseModel):
    inserted_context: StepMemoryRetrievalStepInsertedContext

    memory_bank_ids: List[str]

    step_id: str

    step_type: Literal["memory_retrieval"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None


Step: TypeAlias = Union[StepInferenceStep, StepToolExecutionStep, StepShieldCallStep, StepMemoryRetrievalStep]


class StepRetrieveResponse(BaseModel):
    step: Step

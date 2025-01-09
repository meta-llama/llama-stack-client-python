# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.tool_call import ToolCall
from .shared.interleaved_content import InterleavedContent

__all__ = ["InferenceStep", "ModelResponse"]


class ModelResponse(BaseModel):
    content: InterleavedContent

    role: Literal["assistant"]

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]

    tool_calls: List[ToolCall]


class InferenceStep(BaseModel):
    inference_model_response: ModelResponse = FieldInfo(alias="model_response")

    step_id: str

    step_type: Literal["inference"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

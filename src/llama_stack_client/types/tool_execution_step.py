# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .tool_response import ToolResponse
from .shared.tool_call import ToolCall

__all__ = ["ToolExecutionStep"]


class ToolExecutionStep(BaseModel):
    step_id: str

    step_type: Literal["tool_execution"]

    tool_calls: List[ToolCall]

    tool_responses: List[ToolResponse]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

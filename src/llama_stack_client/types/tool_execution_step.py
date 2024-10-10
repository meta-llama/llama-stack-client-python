# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.tool_call import ToolCall
from .shared.image_media import ImageMedia
from .shared.content_array import ContentArray

__all__ = ["ToolExecutionStep", "ToolResponse", "ToolResponseContent"]

ToolResponseContent: TypeAlias = Union[str, ImageMedia, ContentArray]


class ToolResponse(BaseModel):
    call_id: str

    content: ToolResponseContent

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]


class ToolExecutionStep(BaseModel):
    step_id: str

    step_type: Literal["tool_execution"]

    tool_calls: List[ToolCall]

    tool_responses: List[ToolResponse]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

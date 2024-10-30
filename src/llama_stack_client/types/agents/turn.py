# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..inference_step import InferenceStep
from ..shield_call_step import ShieldCallStep
from ..shared.attachment import Attachment
from ..shared.user_message import UserMessage
from ..tool_execution_step import ToolExecutionStep
from ..memory_retrieval_step import MemoryRetrievalStep
from ..shared.completion_message import CompletionMessage
from ..shared.tool_response_message import ToolResponseMessage

__all__ = ["Turn", "InputMessage", "Step"]

InputMessage: TypeAlias = Union[UserMessage, ToolResponseMessage]

Step: TypeAlias = Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep]


class Turn(BaseModel):
    input_messages: List[InputMessage]

    output_attachments: List[Attachment]

    output_message: CompletionMessage

    session_id: str

    started_at: datetime

    steps: List[Step]

    turn_id: str

    completed_at: Optional[datetime] = None

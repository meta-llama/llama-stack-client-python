# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from ..shared.url import URL
from ..inference_step import InferenceStep
from ..shield_call_step import ShieldCallStep
from ..shared.user_message import UserMessage
from ..tool_execution_step import ToolExecutionStep
from ..memory_retrieval_step import MemoryRetrievalStep
from ..shared.completion_message import CompletionMessage
from ..shared.tool_response_message import ToolResponseMessage
from ..shared.interleaved_content_item import InterleavedContentItem

__all__ = [
    "Turn",
    "InputMessage",
    "OutputAttachment",
    "OutputAttachmentContent",
    "OutputAttachmentContentImageContentItem",
    "OutputAttachmentContentImageContentItemImage",
    "OutputAttachmentContentTextContentItem",
    "Step",
]

InputMessage: TypeAlias = Union[UserMessage, ToolResponseMessage]


class OutputAttachmentContentImageContentItemImage(BaseModel):
    data: Optional[str] = None

    url: Optional[URL] = None


class OutputAttachmentContentImageContentItem(BaseModel):
    image: OutputAttachmentContentImageContentItemImage

    type: Literal["image"]


class OutputAttachmentContentTextContentItem(BaseModel):
    text: str

    type: Literal["text"]


OutputAttachmentContent: TypeAlias = Union[
    str,
    OutputAttachmentContentImageContentItem,
    OutputAttachmentContentTextContentItem,
    List[InterleavedContentItem],
    URL,
]


class OutputAttachment(BaseModel):
    content: OutputAttachmentContent

    mime_type: str


Step: TypeAlias = Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep]


class Turn(BaseModel):
    input_messages: List[InputMessage]

    output_attachments: List[OutputAttachment]

    output_message: CompletionMessage

    session_id: str

    started_at: datetime

    steps: List[Step]

    turn_id: str

    completed_at: Optional[datetime] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .interleaved_content import InterleavedContent

__all__ = ["ToolResponseMessage"]


class ToolResponseMessage(BaseModel):
    call_id: str
    """Unique identifier for the tool call this response is for"""

    content: InterleavedContent
    """The response content from the tool"""

    role: Literal["tool"]
    """Must be "tool" to identify this as a tool response"""

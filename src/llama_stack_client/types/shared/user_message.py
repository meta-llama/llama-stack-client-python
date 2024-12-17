# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .interleaved_content import InterleavedContent

__all__ = ["UserMessage"]


class UserMessage(BaseModel):
    content: InterleavedContent

    role: Literal["user"]

    context: Optional[InterleavedContent] = None

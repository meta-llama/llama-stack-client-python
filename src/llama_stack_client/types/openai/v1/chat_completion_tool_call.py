# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["ChatCompletionToolCall", "Function"]


class Function(BaseModel):
    arguments: Optional[str] = None

    name: Optional[str] = None


class ChatCompletionToolCall(BaseModel):
    type: Literal["function"]

    id: Optional[str] = None

    function: Optional[Function] = None

    index: Optional[int] = None

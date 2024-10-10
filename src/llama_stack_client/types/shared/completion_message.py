# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .tool_call import ToolCall
from .image_media import ImageMedia

__all__ = ["CompletionMessage", "Content", "ContentUnionMember2"]

ContentUnionMember2: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentUnionMember2]]


class CompletionMessage(BaseModel):
    content: Content

    role: Literal["assistant"]

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]

    tool_calls: List[ToolCall]

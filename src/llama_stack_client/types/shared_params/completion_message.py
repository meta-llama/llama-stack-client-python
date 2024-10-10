# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .tool_call import ToolCall
from .image_media import ImageMedia

__all__ = ["CompletionMessage", "Content", "ContentUnionMember2"]

ContentUnionMember2: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentUnionMember2]]


class CompletionMessage(TypedDict, total=False):
    content: Required[Content]

    role: Required[Literal["assistant"]]

    stop_reason: Required[Literal["end_of_turn", "end_of_message", "out_of_tokens"]]

    tool_calls: Required[Iterable[ToolCall]]

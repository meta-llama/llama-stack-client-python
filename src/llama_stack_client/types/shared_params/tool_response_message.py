# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .image_media import ImageMedia

__all__ = ["ToolResponseMessage", "Content", "ContentUnionMember2"]

ContentUnionMember2: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentUnionMember2]]


class ToolResponseMessage(TypedDict, total=False):
    call_id: Required[str]

    content: Required[Content]

    role: Required[Literal["ipython"]]

    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

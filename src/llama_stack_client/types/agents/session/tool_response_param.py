# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

from ...interleaved_content_param import InterleavedContentParam

__all__ = ["ToolResponseParam"]


class ToolResponseParam(TypedDict, total=False):
    call_id: Required[str]

    content: Required[InterleavedContentParam]
    """A image content item"""

    tool_name: Required[Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

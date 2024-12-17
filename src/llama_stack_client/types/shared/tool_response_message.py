# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from ..._models import BaseModel
from .interleaved_content import InterleavedContent

__all__ = ["ToolResponseMessage"]


class ToolResponseMessage(BaseModel):
    call_id: str

    content: InterleavedContent

    role: Literal["ipython"]

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]

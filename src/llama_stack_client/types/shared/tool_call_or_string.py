# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .tool_call import ToolCall

__all__ = ["ToolCallOrString"]

ToolCallOrString: TypeAlias = Union[str, ToolCall]

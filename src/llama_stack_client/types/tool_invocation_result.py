# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel
from .shared.interleaved_content import InterleavedContent

__all__ = ["ToolInvocationResult"]


class ToolInvocationResult(BaseModel):
    content: Optional[InterleavedContent] = None
    """A image content item"""

    error_code: Optional[int] = None

    error_message: Optional[str] = None

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

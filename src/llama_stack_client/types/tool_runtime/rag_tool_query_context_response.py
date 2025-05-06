# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from ..._models import BaseModel
from ..interleaved_content import InterleavedContent

__all__ = ["RagToolQueryContextResponse"]


class RagToolQueryContextResponse(BaseModel):
    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    content: Optional[InterleavedContent] = None
    """A image content item"""

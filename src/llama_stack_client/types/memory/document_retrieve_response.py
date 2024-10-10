# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..shared.image_media import ImageMedia
from ..shared.content_array import ContentArray

__all__ = ["DocumentRetrieveResponse", "Content"]

Content: TypeAlias = Union[str, ImageMedia, ContentArray]


class DocumentRetrieveResponse(BaseModel):
    content: Content

    document_id: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    mime_type: Optional[str] = None

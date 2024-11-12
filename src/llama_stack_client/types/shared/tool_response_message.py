# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .image_media import ImageMedia

__all__ = ["ToolResponseMessage", "Content", "ContentImageMediaArray"]

ContentImageMediaArray: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentImageMediaArray]]


class ToolResponseMessage(BaseModel):
    call_id: str

    content: Content

    role: Literal["ipython"]

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]

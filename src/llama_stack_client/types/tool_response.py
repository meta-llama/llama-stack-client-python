# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.image_media import ImageMedia

__all__ = ["ToolResponse", "Content", "ContentUnionMember2"]

ContentUnionMember2: TypeAlias = Union[str, ImageMedia]

Content: TypeAlias = Union[str, ImageMedia, List[ContentUnionMember2]]


class ToolResponse(BaseModel):
    call_id: str

    content: Content

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel
from .interleaved_content import InterleavedContent

__all__ = ["SystemMessage"]


class SystemMessage(BaseModel):
    content: InterleavedContent

    role: Literal["system"]

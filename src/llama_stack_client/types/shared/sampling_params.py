# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SamplingParams"]


class SamplingParams(BaseModel):
    strategy: Literal["greedy", "top_p", "top_k"]

    max_tokens: Optional[int] = None

    repetition_penalty: Optional[float] = None

    temperature: Optional[float] = None

    top_k: Optional[int] = None

    top_p: Optional[float] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .completion_response import CompletionResponse

__all__ = ["InferenceBatchCompletionResponse"]


class InferenceBatchCompletionResponse(BaseModel):
    batch: List[CompletionResponse]

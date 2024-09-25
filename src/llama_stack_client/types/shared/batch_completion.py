# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .completion_message import CompletionMessage

__all__ = ["BatchCompletion"]


class BatchCompletion(BaseModel):
    completion_message_batch: List[CompletionMessage]

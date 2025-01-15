# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .eval_task import EvalTask

__all__ = ["EvalTaskListResponse"]


class EvalTaskListResponse(BaseModel):
    data: List[EvalTask]

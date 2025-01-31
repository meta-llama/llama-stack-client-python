# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .eval_task_list_response import EvalTaskListResponse

__all__ = ["ListEvalTasksResponse"]


class ListEvalTasksResponse(BaseModel):
    data: EvalTaskListResponse

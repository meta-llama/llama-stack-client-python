# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .scoring_function_list_response import ScoringFunctionListResponse

__all__ = ["ListScoringFunctionsResponse"]


class ListScoringFunctionsResponse(BaseModel):
    data: ScoringFunctionListResponse

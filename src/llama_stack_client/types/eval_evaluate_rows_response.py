# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel
from .shared.scoring_result import ScoringResult

__all__ = ["EvalEvaluateRowsResponse"]


class EvalEvaluateRowsResponse(BaseModel):
    generations: List[Dict[str, Union[bool, float, str, List[object], object, None]]]

    scores: Dict[str, ScoringResult]
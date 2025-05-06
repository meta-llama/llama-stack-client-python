# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["ScoringScoreResponse", "Results"]


class Results(BaseModel):
    aggregated_results: Dict[str, Union[bool, float, str, List[object], object, None]]
    """Map of metric name to aggregated value"""

    score_rows: List[Dict[str, Union[bool, float, str, List[object], object, None]]]
    """The scoring result for each row. Each row is a map of column name to value."""


class ScoringScoreResponse(BaseModel):
    results: Dict[str, Results]
    """A map of scoring function name to ScoringResult."""

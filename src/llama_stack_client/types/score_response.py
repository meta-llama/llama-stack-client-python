# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["ScoreResponse", "Results"]


class Results(BaseModel):
    aggregated_results: Dict[str, Union[bool, float, str, List[object], object, None]]

    score_rows: List[Dict[str, Union[bool, float, str, List[object], object, None]]]


class ScoreResponse(BaseModel):
    results: Dict[str, Results]

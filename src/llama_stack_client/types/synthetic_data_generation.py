# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel
from .scored_dialog_generations import ScoredDialogGenerations

__all__ = ["SyntheticDataGeneration"]


class SyntheticDataGeneration(BaseModel):
    synthetic_data: List[ScoredDialogGenerations]

    statistics: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

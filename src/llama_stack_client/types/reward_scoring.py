# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .scored_dialog_generations import ScoredDialogGenerations

__all__ = ["RewardScoring"]


class RewardScoring(BaseModel):
    scored_generations: List[ScoredDialogGenerations]

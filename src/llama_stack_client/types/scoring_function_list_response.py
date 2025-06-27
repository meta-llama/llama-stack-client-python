# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .scoring_fn import ScoringFn

__all__ = ["ScoringFunctionListResponse"]

ScoringFunctionListResponse: TypeAlias = List[ScoringFn]

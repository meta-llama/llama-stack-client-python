# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "SamplingParams",
    "Strategy",
    "StrategyGreedySamplingStrategy",
    "StrategyTopPSamplingStrategy",
    "StrategyTopKSamplingStrategy",
]


class StrategyGreedySamplingStrategy(BaseModel):
    type: Literal["greedy"]


class StrategyTopPSamplingStrategy(BaseModel):
    type: Literal["top_p"]

    temperature: Optional[float] = None

    top_p: Optional[float] = None


class StrategyTopKSamplingStrategy(BaseModel):
    top_k: int

    type: Literal["top_k"]


Strategy: TypeAlias = Annotated[
    Union[StrategyGreedySamplingStrategy, StrategyTopPSamplingStrategy, StrategyTopKSamplingStrategy],
    PropertyInfo(discriminator="type"),
]


class SamplingParams(BaseModel):
    strategy: Strategy

    max_tokens: Optional[int] = None

    repetition_penalty: Optional[float] = None

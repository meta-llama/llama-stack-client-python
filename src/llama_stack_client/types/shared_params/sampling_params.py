# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "SamplingParams",
    "Strategy",
    "StrategyGreedySamplingStrategy",
    "StrategyTopPSamplingStrategy",
    "StrategyTopKSamplingStrategy",
]


class StrategyGreedySamplingStrategy(TypedDict, total=False):
    type: Required[Literal["greedy"]]


class StrategyTopPSamplingStrategy(TypedDict, total=False):
    type: Required[Literal["top_p"]]

    temperature: float

    top_p: float


class StrategyTopKSamplingStrategy(TypedDict, total=False):
    top_k: Required[int]

    type: Required[Literal["top_k"]]


Strategy: TypeAlias = Union[StrategyGreedySamplingStrategy, StrategyTopPSamplingStrategy, StrategyTopKSamplingStrategy]


class SamplingParams(TypedDict, total=False):
    strategy: Required[Strategy]
    """The sampling strategy."""

    max_tokens: int
    """The maximum number of tokens that can be generated in the completion.

    The token count of your prompt plus max_tokens cannot exceed the model's context
    length.
    """

    repetition_penalty: float
    """Number between -2.0 and 2.0.

    Positive values penalize new tokens based on whether they appear in the text so
    far, increasing the model's likelihood to talk about new topics.
    """

    stop: List[str]
    """Up to 4 sequences where the API will stop generating further tokens.

    The returned text will not contain the stop sequence.
    """

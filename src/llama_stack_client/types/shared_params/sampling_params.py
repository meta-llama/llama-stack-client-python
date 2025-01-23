# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["SamplingParams", "Strategy", "StrategyGreedy", "StrategyTopP", "StrategyTopK"]


class StrategyGreedy(TypedDict, total=False):
    type: Required[Literal["greedy"]]


class StrategyTopP(TypedDict, total=False):
    type: Required[Literal["top_p"]]

    temperature: float

    top_p: float


class StrategyTopK(TypedDict, total=False):
    top_k: Required[int]

    type: Required[Literal["top_k"]]


Strategy: TypeAlias = Union[StrategyGreedy, StrategyTopP, StrategyTopK]


class SamplingParams(TypedDict, total=False):
    strategy: Required[Strategy]

    max_tokens: int

    repetition_penalty: float

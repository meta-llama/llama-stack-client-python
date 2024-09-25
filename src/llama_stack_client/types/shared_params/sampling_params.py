# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SamplingParams"]


class SamplingParams(TypedDict, total=False):
    strategy: Required[Literal["greedy", "top_p", "top_k"]]

    max_tokens: int

    repetition_penalty: float

    temperature: float

    top_k: int

    top_p: float

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["BenchmarkRegisterParams"]


class BenchmarkRegisterParams(TypedDict, total=False):
    benchmark_id: Required[str]

    dataset_id: Required[str]

    scoring_functions: Required[List[str]]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    provider_benchmark_id: str

    provider_id: str

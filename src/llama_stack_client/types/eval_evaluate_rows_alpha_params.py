# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, TypedDict

from .benchmark_config_param import BenchmarkConfigParam

__all__ = ["EvalEvaluateRowsAlphaParams"]


class EvalEvaluateRowsAlphaParams(TypedDict, total=False):
    input_rows: Required[Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]]

    scoring_functions: Required[List[str]]

    task_config: Required[BenchmarkConfigParam]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["EvalTaskRegisterParams"]


class EvalTaskRegisterParams(TypedDict, total=False):
    dataset_id: Required[str]

    scoring_functions: Required[List[str]]

    task_id: Required[str]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    provider_eval_task_id: str

    provider_id: str

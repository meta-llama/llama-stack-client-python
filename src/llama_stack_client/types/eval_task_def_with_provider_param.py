# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EvalTaskDefWithProviderParam"]


class EvalTaskDefWithProviderParam(TypedDict, total=False):
    dataset_id: Required[str]

    identifier: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    provider_id: Required[str]

    scoring_functions: Required[List[str]]

    type: Required[Literal["eval_task"]]

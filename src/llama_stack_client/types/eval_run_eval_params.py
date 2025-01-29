# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .eval_task_config_param import EvalTaskConfigParam

__all__ = ["EvalRunEvalParams"]


class EvalRunEvalParams(TypedDict, total=False):
    task_config: Required[EvalTaskConfigParam]

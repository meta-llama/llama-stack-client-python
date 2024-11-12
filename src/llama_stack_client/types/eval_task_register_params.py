# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvalTaskRegisterParams"]


class EvalTaskRegisterParams(TypedDict, total=False):
    dataset_id: Required[str]

    eval_task_id: Required[str]

    scoring_functions: Required[List[str]]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    provider_eval_task_id: str

    provider_id: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

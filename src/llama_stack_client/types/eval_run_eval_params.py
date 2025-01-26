# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .eval_task_config_param import EvalTaskConfigParam

__all__ = ["EvalRunEvalParams"]


class EvalRunEvalParams(TypedDict, total=False):
    task_config: Required[EvalTaskConfigParam]

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]

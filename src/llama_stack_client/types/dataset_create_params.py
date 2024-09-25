# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .train_eval_dataset_param import TrainEvalDatasetParam

__all__ = ["DatasetCreateParams"]


class DatasetCreateParams(TypedDict, total=False):
    dataset: Required[TrainEvalDatasetParam]

    uuid: Required[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

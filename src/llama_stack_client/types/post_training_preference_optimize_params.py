# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PostTrainingPreferenceOptimizeParams", "AlgorithmConfig", "OptimizerConfig", "TrainingConfig"]


class PostTrainingPreferenceOptimizeParams(TypedDict, total=False):
    algorithm: Required[Literal["dpo"]]

    algorithm_config: Required[AlgorithmConfig]

    dataset_id: Required[str]

    finetuned_model: Required[str]

    hyperparam_search_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    job_uuid: Required[str]

    logger_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    optimizer_config: Required[OptimizerConfig]

    training_config: Required[TrainingConfig]

    validation_dataset_id: Required[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class AlgorithmConfig(TypedDict, total=False):
    epsilon: Required[float]

    gamma: Required[float]

    reward_clip: Required[float]

    reward_scale: Required[float]


class OptimizerConfig(TypedDict, total=False):
    lr: Required[float]

    lr_min: Required[float]

    optimizer_type: Required[Literal["adam", "adamw", "sgd"]]

    weight_decay: Required[float]


class TrainingConfig(TypedDict, total=False):
    batch_size: Required[int]

    enable_activation_checkpointing: Required[bool]

    fsdp_cpu_offload: Required[bool]

    memory_efficient_fsdp_wrap: Required[bool]

    n_epochs: Required[int]

    n_iters: Required[int]

    shuffle: Required[bool]

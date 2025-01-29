# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = [
    "PostTrainingPreferenceOptimizeParams",
    "AlgorithmConfig",
    "TrainingConfig",
    "TrainingConfigDataConfig",
    "TrainingConfigOptimizerConfig",
    "TrainingConfigEfficiencyConfig",
]


class PostTrainingPreferenceOptimizeParams(TypedDict, total=False):
    algorithm_config: Required[AlgorithmConfig]

    finetuned_model: Required[str]

    hyperparam_search_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    job_uuid: Required[str]

    logger_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    training_config: Required[TrainingConfig]


class AlgorithmConfig(TypedDict, total=False):
    epsilon: Required[float]

    gamma: Required[float]

    reward_clip: Required[float]

    reward_scale: Required[float]


class TrainingConfigDataConfig(TypedDict, total=False):
    batch_size: Required[int]

    data_format: Required[Literal["instruct", "dialog"]]

    dataset_id: Required[str]

    shuffle: Required[bool]

    packed: bool

    train_on_input: bool

    validation_dataset_id: str


class TrainingConfigOptimizerConfig(TypedDict, total=False):
    lr: Required[float]

    num_warmup_steps: Required[int]

    optimizer_type: Required[Literal["adam", "adamw", "sgd"]]

    weight_decay: Required[float]


class TrainingConfigEfficiencyConfig(TypedDict, total=False):
    enable_activation_checkpointing: bool

    enable_activation_offloading: bool

    fsdp_cpu_offload: bool

    memory_efficient_fsdp_wrap: bool


class TrainingConfig(TypedDict, total=False):
    data_config: Required[TrainingConfigDataConfig]

    gradient_accumulation_steps: Required[int]

    max_steps_per_epoch: Required[int]

    max_validation_steps: Required[int]

    n_epochs: Required[int]

    optimizer_config: Required[TrainingConfigOptimizerConfig]

    dtype: str

    efficiency_config: TrainingConfigEfficiencyConfig

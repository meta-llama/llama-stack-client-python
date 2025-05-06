# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrainingConfigParam", "DataConfig", "EfficiencyConfig", "OptimizerConfig"]


class DataConfig(TypedDict, total=False):
    batch_size: Required[int]

    data_format: Required[Literal["instruct", "dialog"]]

    dataset_id: Required[str]

    shuffle: Required[bool]

    packed: bool

    train_on_input: bool

    validation_dataset_id: str


class EfficiencyConfig(TypedDict, total=False):
    enable_activation_checkpointing: bool

    enable_activation_offloading: bool

    fsdp_cpu_offload: bool

    memory_efficient_fsdp_wrap: bool


class OptimizerConfig(TypedDict, total=False):
    lr: Required[float]

    num_warmup_steps: Required[int]

    optimizer_type: Required[Literal["adam", "adamw", "sgd"]]

    weight_decay: Required[float]


class TrainingConfigParam(TypedDict, total=False):
    gradient_accumulation_steps: Required[int]

    max_steps_per_epoch: Required[int]

    n_epochs: Required[int]

    data_config: DataConfig

    dtype: str

    efficiency_config: EfficiencyConfig

    max_validation_steps: int

    optimizer_config: OptimizerConfig

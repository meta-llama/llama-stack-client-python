# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "PostTrainingSupervisedFineTuneParams",
    "TrainingConfig",
    "TrainingConfigDataConfig",
    "TrainingConfigOptimizerConfig",
    "TrainingConfigEfficiencyConfig",
    "AlgorithmConfig",
    "AlgorithmConfigLoraFinetuningConfig",
    "AlgorithmConfigQatFinetuningConfig",
]


class PostTrainingSupervisedFineTuneParams(TypedDict, total=False):
    hyperparam_search_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    job_uuid: Required[str]

    logger_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    model: Required[str]

    training_config: Required[TrainingConfig]

    algorithm_config: AlgorithmConfig

    checkpoint_dir: str


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


class AlgorithmConfigLoraFinetuningConfig(TypedDict, total=False):
    alpha: Required[int]

    apply_lora_to_mlp: Required[bool]

    apply_lora_to_output: Required[bool]

    lora_attn_modules: Required[List[str]]

    rank: Required[int]

    type: Required[Literal["LoRA"]]

    quantize_base: bool

    use_dora: bool


class AlgorithmConfigQatFinetuningConfig(TypedDict, total=False):
    group_size: Required[int]

    quantizer_name: Required[str]

    type: Required[Literal["QAT"]]


AlgorithmConfig: TypeAlias = Union[AlgorithmConfigLoraFinetuningConfig, AlgorithmConfigQatFinetuningConfig]

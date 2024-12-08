# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, List, Union

from typing_extensions import Annotated, Literal, Required, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PostTrainingSupervisedFineTuneParams",
    "AlgorithmConfig",
    "AlgorithmConfigLoraFinetuningConfig",
    "AlgorithmConfigQATFinetuningConfig",
    "DataConfig",
    "EfficienctConfig",
    "OptimizerConfig",
    "TrainingConfig",
]


class PostTrainingSupervisedFineTuneParams(TypedDict, total=False):
    algorithm: Required[Literal["full", "lora", "qat"]]

    algorithm_config: AlgorithmConfig

    hyperparam_search_config: Required[
        Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    ]

    job_uuid: Required[str]

    logger_config: Required[
        Dict[str, Union[bool, float, str, Iterable[object], object, None]]
    ]

    model: Required[str]

    training_config: Required[TrainingConfig]

    x_llama_stack_provider_data: Annotated[
        str, PropertyInfo(alias="X-LlamaStack-ProviderData")
    ]


class AlgorithmConfigLoraFinetuningConfig(TypedDict, total=False):
    alpha: Required[int]

    apply_lora_to_mlp: Required[bool]

    apply_lora_to_output: Required[bool]

    lora_attn_modules: Required[List[str]]

    rank: Required[int]

    use_dora: bool

    quantize_base: bool


class AlgorithmConfigQATFinetuningConfig(TypedDict, total=False):
    quantizer_name: Required[str]
    group_size: Required[int]


AlgorithmConfig: TypeAlias = Union[
    AlgorithmConfigLoraFinetuningConfig,
    AlgorithmConfigQATFinetuningConfig,
]


class DataConfig(TypedDict, total=False):
    dataset_id: Required[str]

    batch_size: Required[int]

    shuffle: Required[bool]

    validation_dataset_id: str

    packed: bool

    train_on_input: bool


class EfficienctConfig(TypedDict, total=False):
    enable_activation_checkpointing: bool

    enable_activation_offloading: bool

    memory_efficient_fsdp_wrap: bool

    fsdp_cpu_offload: bool


class OptimizerConfig(TypedDict, total=False):
    lr: Required[float]

    lr_min: Required[float]

    optimizer_type: Required[Literal["adam", "adamw", "sgd"]]

    weight_decay: Required[float]

    num_warmup_steps: Required[int]


class TrainingConfig(TypedDict, total=False):
    n_epochs: Required[int]

    data_config: Required[DataConfig]

    optimizer_config: Required[OptimizerConfig]

    efficient_config: EfficienctConfig

    max_steps_per_epoch: Required[int]

    gradient_accumulation_steps: Required[int]

    dtype: Literal["bf16", "fp16", "fp32"]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PostTrainingSupervisedFineTuneParams",
    "AlgorithmConfig",
    "AlgorithmConfigLoraFinetuningConfig",
    "AlgorithmConfigQLoraFinetuningConfig",
    "AlgorithmConfigDoraFinetuningConfig",
    "OptimizerConfig",
    "TrainingConfig",
]


class PostTrainingSupervisedFineTuneParams(TypedDict, total=False):
    algorithm: Required[Literal["full", "lora", "qlora", "dora"]]

    algorithm_config: Required[AlgorithmConfig]

    dataset_id: Required[str]

    hyperparam_search_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    job_uuid: Required[str]

    logger_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    model: Required[str]

    optimizer_config: Required[OptimizerConfig]

    training_config: Required[TrainingConfig]

    validation_dataset_id: Required[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


class AlgorithmConfigLoraFinetuningConfig(TypedDict, total=False):
    alpha: Required[int]

    apply_lora_to_mlp: Required[bool]

    apply_lora_to_output: Required[bool]

    lora_attn_modules: Required[List[str]]

    rank: Required[int]


class AlgorithmConfigQLoraFinetuningConfig(TypedDict, total=False):
    alpha: Required[int]

    apply_lora_to_mlp: Required[bool]

    apply_lora_to_output: Required[bool]

    lora_attn_modules: Required[List[str]]

    rank: Required[int]


class AlgorithmConfigDoraFinetuningConfig(TypedDict, total=False):
    alpha: Required[int]

    apply_lora_to_mlp: Required[bool]

    apply_lora_to_output: Required[bool]

    lora_attn_modules: Required[List[str]]

    rank: Required[int]


AlgorithmConfig: TypeAlias = Union[
    AlgorithmConfigLoraFinetuningConfig, AlgorithmConfigQLoraFinetuningConfig, AlgorithmConfigDoraFinetuningConfig
]


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

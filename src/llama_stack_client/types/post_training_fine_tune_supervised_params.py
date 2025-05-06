# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .training_config_param import TrainingConfigParam

__all__ = [
    "PostTrainingFineTuneSupervisedParams",
    "AlgorithmConfig",
    "AlgorithmConfigLoraFinetuningConfig",
    "AlgorithmConfigQatFinetuningConfig",
]


class PostTrainingFineTuneSupervisedParams(TypedDict, total=False):
    hyperparam_search_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    job_uuid: Required[str]

    logger_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    training_config: Required[TrainingConfigParam]

    algorithm_config: AlgorithmConfig

    checkpoint_dir: str

    model: str


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

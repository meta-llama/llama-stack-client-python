# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["AlgorithmConfigParam", "LoraFinetuningConfig", "QatFinetuningConfig"]


class LoraFinetuningConfig(TypedDict, total=False):
    alpha: Required[int]

    apply_lora_to_mlp: Required[bool]

    apply_lora_to_output: Required[bool]

    lora_attn_modules: Required[List[str]]

    rank: Required[int]

    type: Required[Literal["LoRA"]]

    quantize_base: bool

    use_dora: bool


class QatFinetuningConfig(TypedDict, total=False):
    group_size: Required[int]

    quantizer_name: Required[str]

    type: Required[Literal["QAT"]]


AlgorithmConfigParam: TypeAlias = Union[LoraFinetuningConfig, QatFinetuningConfig]

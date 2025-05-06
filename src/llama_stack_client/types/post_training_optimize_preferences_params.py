# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .training_config_param import TrainingConfigParam

__all__ = ["PostTrainingOptimizePreferencesParams", "AlgorithmConfig"]


class PostTrainingOptimizePreferencesParams(TypedDict, total=False):
    algorithm_config: Required[AlgorithmConfig]

    finetuned_model: Required[str]

    hyperparam_search_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    job_uuid: Required[str]

    logger_config: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    training_config: Required[TrainingConfigParam]


class AlgorithmConfig(TypedDict, total=False):
    epsilon: Required[float]

    gamma: Required[float]

    reward_clip: Required[float]

    reward_scale: Required[float]

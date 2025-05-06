# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .model_type import ModelType

__all__ = ["ModelCreateParams"]


class ModelCreateParams(TypedDict, total=False):
    model_id: Required[str]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    model_type: ModelType

    provider_id: str

    provider_model_id: str

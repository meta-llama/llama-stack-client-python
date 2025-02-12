# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.param_type import ParamType

__all__ = ["DatasetRegisterParams", "URL"]


class DatasetRegisterParams(TypedDict, total=False):
    dataset_id: Required[str]

    dataset_schema: Required[Dict[str, ParamType]]

    url: Required[URL]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    provider_dataset_id: str

    provider_id: str


class URL(TypedDict, total=False):
    uri: Required[str]

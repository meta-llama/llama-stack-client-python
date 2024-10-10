# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ModelDefWithProviderParam"]


class ModelDefWithProviderParam(TypedDict, total=False):
    identifier: Required[str]

    llama_model: Required[str]

    metadata: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    provider_id: Required[str]

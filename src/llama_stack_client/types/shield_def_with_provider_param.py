# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ShieldDefWithProviderParam"]


class ShieldDefWithProviderParam(TypedDict, total=False):
    identifier: Required[str]

    params: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    provider_id: Required[str]

    type: Required[str]

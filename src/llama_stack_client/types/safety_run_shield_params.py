# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.message import Message

__all__ = ["SafetyRunShieldParams"]


class SafetyRunShieldParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    params: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    shield_id: Required[str]

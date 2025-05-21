# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .shared_params.message import Message

__all__ = ["SafetyRunShieldParams"]


class SafetyRunShieldParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]
    """The messages to run the shield on."""

    params: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]
    """The parameters of the shield."""

    shield_id: Required[str]
    """The identifier of the shield to run."""

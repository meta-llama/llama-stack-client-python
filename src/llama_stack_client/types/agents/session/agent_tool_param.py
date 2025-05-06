# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["AgentToolParam", "AgentToolGroupWithArgs"]


class AgentToolGroupWithArgs(TypedDict, total=False):
    args: Required[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]

    name: Required[str]


AgentToolParam: TypeAlias = Union[str, AgentToolGroupWithArgs]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["GraphMemoryBankDef"]


class GraphMemoryBankDef(TypedDict, total=False):
    identifier: Required[str]

    provider_id: Required[str]

    type: Required[Literal["graph"]]

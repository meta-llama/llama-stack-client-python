# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["SessionRetrieveParams"]


class SessionRetrieveParams(TypedDict, total=False):
    agent_id: Required[str]

    turn_ids: List[str]
    """(Optional) List of turn IDs to filter the session by."""

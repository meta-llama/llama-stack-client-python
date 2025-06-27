# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import builtins
from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["VectorStore", "FileCounts"]


class FileCounts(BaseModel):
    cancelled: int

    completed: int

    failed: int

    in_progress: int

    total: int


class VectorStore(BaseModel):
    id: str

    created_at: int

    file_counts: FileCounts

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    object: str

    status: str

    usage_bytes: int

    expires_after: Optional[Dict[str, Union[bool, float, str, List[builtins.object], builtins.object, None]]] = None

    expires_at: Optional[int] = None

    last_active_at: Optional[int] = None

    name: Optional[str] = None

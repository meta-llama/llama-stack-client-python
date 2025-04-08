# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["JobStatusResponse"]


class JobStatusResponse(BaseModel):
    checkpoints: List[object]

    job_uuid: str

    status: Literal["completed", "in_progress", "failed", "scheduled", "cancelled"]

    completed_at: Optional[datetime] = None

    resources_allocated: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    scheduled_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

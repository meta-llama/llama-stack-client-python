# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["JobLogsResponse"]


class JobLogsResponse(BaseModel):
    job_uuid: str

    log_lines: List[str]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["JobArtifactsResponse"]


class JobArtifactsResponse(BaseModel):
    checkpoints: List[object]

    job_uuid: str

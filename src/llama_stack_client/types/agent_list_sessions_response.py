# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .agents.session.session import Session

__all__ = ["AgentListSessionsResponse"]


class AgentListSessionsResponse(BaseModel):
    data: List[Session]

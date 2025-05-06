# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .agent import Agent
from .._models import BaseModel

__all__ = ["AgentListResponse"]


class AgentListResponse(BaseModel):
    data: List[Agent]

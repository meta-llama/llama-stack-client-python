# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel
from .agent_config import AgentConfig

__all__ = ["Agent"]


class Agent(BaseModel):
    agent_config: AgentConfig
    """Configuration for an agent."""

    agent_id: str

    created_at: datetime

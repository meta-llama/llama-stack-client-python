# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .agent_config_param import AgentConfigParam

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    agent_config: Required[AgentConfigParam]
    """The configuration for the agent."""

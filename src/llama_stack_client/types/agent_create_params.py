# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.agent_config import AgentConfig

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    agent_config: Required[AgentConfig]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

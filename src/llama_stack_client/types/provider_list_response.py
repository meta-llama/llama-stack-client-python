# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .provider_info import ProviderInfo

__all__ = ["ProviderListResponse"]

ProviderListResponse: TypeAlias = Dict[str, ProviderInfo]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .provider_info import ProviderInfo

__all__ = ["ListProvidersResponse"]


class ListProvidersResponse(BaseModel):
    data: List[ProviderInfo]
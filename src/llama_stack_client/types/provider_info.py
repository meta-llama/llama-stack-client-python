# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from typing import Dict, Any

__all__ = ["ProviderInfo"]


class ProviderInfo(BaseModel):
    api: str

    provider_id: str

    provider_type: str

class ProviderInfoWithConfig(BaseModel):
    api: str

    provider_id: str

    provider_type: str

    config: Dict[str, Any]

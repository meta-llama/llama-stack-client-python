# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["ShieldSpec", "ProviderConfig"]


class ProviderConfig(BaseModel):
    config: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_type: str


class ShieldSpec(BaseModel):
    provider_config: ProviderConfig

    shield_type: str

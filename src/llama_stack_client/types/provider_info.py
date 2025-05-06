# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["ProviderInfo"]


class ProviderInfo(BaseModel):
    api: str

    config: Dict[str, Union[bool, float, str, List[object], object, None]]

    health: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    provider_type: str

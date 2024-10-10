# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MemoryBankSpec", "ProviderConfig"]


class ProviderConfig(BaseModel):
    config: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_type: str


class MemoryBankSpec(BaseModel):
    bank_type: Literal["vector", "keyvalue", "keyword", "graph"]

    provider_config: ProviderConfig

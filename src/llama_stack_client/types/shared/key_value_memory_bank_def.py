# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KeyValueMemoryBankDef"]


class KeyValueMemoryBankDef(BaseModel):
    identifier: str

    provider_id: str

    type: Literal["keyvalue"]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["ShieldDefWithProvider"]


class ShieldDefWithProvider(BaseModel):
    identifier: str

    params: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    type: str

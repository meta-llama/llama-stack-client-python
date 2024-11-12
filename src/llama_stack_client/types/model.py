# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Model"]


class Model(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    provider_resource_id: str

    type: Literal["model"]

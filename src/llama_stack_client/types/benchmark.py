# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Benchmark"]


class Benchmark(BaseModel):
    dataset_id: str

    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    scoring_functions: List[str]

    type: Literal["benchmark"]

    provider_resource_id: Optional[str] = None

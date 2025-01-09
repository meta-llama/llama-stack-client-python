# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal

from .._models import BaseModel
from .shared.url import URL
from .shared.param_type import ParamType

__all__ = ["DatasetRetrieveResponse"]


class DatasetRetrieveResponse(BaseModel):
    dataset_schema: Dict[str, ParamType]

    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    provider_resource_id: str

    type: Literal["dataset"]

    url: URL

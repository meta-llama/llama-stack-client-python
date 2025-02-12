# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.param_type import ParamType

__all__ = ["DatasetListResponse", "DatasetListResponseItem", "DatasetListResponseItemURL"]


class DatasetListResponseItemURL(BaseModel):
    uri: str


class DatasetListResponseItem(BaseModel):
    dataset_schema: Dict[str, ParamType]

    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    provider_resource_id: str

    type: Literal["dataset"]

    url: DatasetListResponseItemURL


DatasetListResponse: TypeAlias = List[DatasetListResponseItem]

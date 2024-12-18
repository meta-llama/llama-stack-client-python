# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.url import URL
from .shared_params.param_type import ParamType

__all__ = ["DatasetRegisterParams"]


class DatasetRegisterParams(TypedDict, total=False):
    dataset_id: Required[str]

    dataset_schema: Required[Dict[str, ParamType]]

    url: Required[URL]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    provider_dataset_id: str

    provider_id: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

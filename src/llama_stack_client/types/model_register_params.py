# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ModelRegisterParams"]


class ModelRegisterParams(TypedDict, total=False):
    model_id: Required[str]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    provider_id: str

    provider_model_id: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

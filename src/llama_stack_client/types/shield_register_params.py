# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ShieldRegisterParams"]


class ShieldRegisterParams(TypedDict, total=False):
    shield_id: Required[str]

    params: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    provider_id: str

    provider_shield_id: str

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

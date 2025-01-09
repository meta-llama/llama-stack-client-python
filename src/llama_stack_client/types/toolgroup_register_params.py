# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.url import URL

__all__ = ["ToolgroupRegisterParams"]


class ToolgroupRegisterParams(TypedDict, total=False):
    provider_id: Required[str]

    toolgroup_id: Required[str]

    args: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    mcp_endpoint: URL

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]

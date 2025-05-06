# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, TypedDict

from .url_param import URLParam

__all__ = ["ToolgroupRegisterParams"]


class ToolgroupRegisterParams(TypedDict, total=False):
    provider_id: Required[str]

    toolgroup_id: Required[str]

    args: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    mcp_endpoint: URLParam

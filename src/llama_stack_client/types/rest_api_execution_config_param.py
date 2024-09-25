# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RestAPIExecutionConfigParam"]


class RestAPIExecutionConfigParam(TypedDict, total=False):
    method: Required[Literal["GET", "POST", "PUT", "DELETE"]]

    url: Required[str]

    body: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    headers: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

    params: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

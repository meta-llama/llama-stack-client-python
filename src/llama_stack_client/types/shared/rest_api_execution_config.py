# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .url import URL
from ..._models import BaseModel

__all__ = ["RestAPIExecutionConfig"]


class RestAPIExecutionConfig(BaseModel):
    method: Literal["GET", "POST", "PUT", "DELETE"]

    url: URL

    body: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    headers: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

    params: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import TypeAlias

from .route_info import RouteInfo

__all__ = ["RouteListResponse"]

RouteListResponse: TypeAlias = Dict[str, List[RouteInfo]]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RunSheidResponse", "Violation"]


class Violation(BaseModel):
    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    violation_level: Literal["info", "warn", "error"]

    user_message: Optional[str] = None


class RunSheidResponse(BaseModel):
    violation: Optional[Violation] = None

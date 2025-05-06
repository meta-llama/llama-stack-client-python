# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .safety_violation import SafetyViolation

__all__ = ["SafetyRunShieldResponse"]


class SafetyRunShieldResponse(BaseModel):
    violation: Optional[SafetyViolation] = None

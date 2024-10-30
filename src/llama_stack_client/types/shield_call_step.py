# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .shared.safety_violation import SafetyViolation

__all__ = ["ShieldCallStep"]


class ShieldCallStep(BaseModel):
    step_id: str

    step_type: Literal["shield_call"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

    violation: Optional[SafetyViolation] = None

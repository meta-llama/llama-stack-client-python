# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ShieldCallStep", "Violation"]


class Violation(BaseModel):
    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    violation_level: Literal["info", "warn", "error"]

    user_message: Optional[str] = None


class ShieldCallStep(BaseModel):
    step_id: str

    step_type: Literal["shield_call"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

    violation: Optional[Violation] = None

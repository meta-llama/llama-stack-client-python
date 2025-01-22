# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.completion_message import CompletionMessage

__all__ = ["InferenceStep"]


class InferenceStep(BaseModel):
    inference_model_response: CompletionMessage = FieldInfo(alias="model_response")

    step_id: str

    step_type: Literal["inference"]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

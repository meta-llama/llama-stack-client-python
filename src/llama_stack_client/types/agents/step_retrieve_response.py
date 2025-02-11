# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel
from ..inference_step import InferenceStep
from ..shield_call_step import ShieldCallStep
from ..tool_execution_step import ToolExecutionStep
from ..memory_retrieval_step import MemoryRetrievalStep

__all__ = ["StepRetrieveResponse", "Step", "Metric"]

Step: TypeAlias = Annotated[
    Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep],
    PropertyInfo(discriminator="step_type"),
]


class Metric(BaseModel):
    metric: str

    span_id: str

    timestamp: datetime

    trace_id: str

    type: Literal["metric"]

    unit: str

    value: float

    attributes: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None


class StepRetrieveResponse(BaseModel):
    step: Step

    metrics: Optional[List[Metric]] = None

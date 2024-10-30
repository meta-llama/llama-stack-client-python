# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from ..._models import BaseModel
from ..inference_step import InferenceStep
from ..shield_call_step import ShieldCallStep
from ..tool_execution_step import ToolExecutionStep
from ..memory_retrieval_step import MemoryRetrievalStep

__all__ = ["StepRetrieveResponse", "Step"]

Step: TypeAlias = Union[InferenceStep, ToolExecutionStep, ShieldCallStep, MemoryRetrievalStep]


class StepRetrieveResponse(BaseModel):
    step: Step

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.tool_call import ToolCall

__all__ = [
    "ToolExecutionStep",
    "ToolResponse",
    "ToolResponseContent",
    "ToolResponseContentImageMedia",
    "ToolResponseContentImageMediaImage",
    "ToolResponseContentImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "ToolResponseContentUnionMember2",
    "ToolResponseContentUnionMember2ImageMedia",
    "ToolResponseContentUnionMember2ImageMediaImage",
    "ToolResponseContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
]


class ToolResponseContentImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


ToolResponseContentImageMediaImage: TypeAlias = Union[
    ToolResponseContentImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class ToolResponseContentImageMedia(BaseModel):
    image: ToolResponseContentImageMediaImage


class ToolResponseContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


ToolResponseContentUnionMember2ImageMediaImage: TypeAlias = Union[
    ToolResponseContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class ToolResponseContentUnionMember2ImageMedia(BaseModel):
    image: ToolResponseContentUnionMember2ImageMediaImage


ToolResponseContentUnionMember2: TypeAlias = Union[str, ToolResponseContentUnionMember2ImageMedia]

ToolResponseContent: TypeAlias = Union[str, ToolResponseContentImageMedia, List[ToolResponseContentUnionMember2]]


class ToolResponse(BaseModel):
    call_id: str

    content: ToolResponseContent

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]


class ToolExecutionStep(BaseModel):
    step_id: str

    step_type: Literal["tool_execution"]

    tool_calls: List[ToolCall]

    tool_responses: List[ToolResponse]

    turn_id: str

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

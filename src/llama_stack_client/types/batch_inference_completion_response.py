# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "BatchInferenceCompletionResponse",
    "CompletionMessageBatch",
    "CompletionMessageBatchContent",
    "CompletionMessageBatchContentImageMedia",
    "CompletionMessageBatchContentImageMediaImage",
    "CompletionMessageBatchContentImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "CompletionMessageBatchContentUnionMember2",
    "CompletionMessageBatchContentUnionMember2ImageMedia",
    "CompletionMessageBatchContentUnionMember2ImageMediaImage",
    "CompletionMessageBatchContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate",
    "CompletionMessageBatchToolCall",
]


class CompletionMessageBatchContentImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


CompletionMessageBatchContentImageMediaImage: TypeAlias = Union[
    CompletionMessageBatchContentImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class CompletionMessageBatchContentImageMedia(BaseModel):
    image: CompletionMessageBatchContentImageMediaImage


class CompletionMessageBatchContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate(BaseModel):
    format: Optional[str] = None

    format_description: Optional[str] = None


CompletionMessageBatchContentUnionMember2ImageMediaImage: TypeAlias = Union[
    CompletionMessageBatchContentUnionMember2ImageMediaImageThisClassRepresentsAnImageObjectToCreate, str
]


class CompletionMessageBatchContentUnionMember2ImageMedia(BaseModel):
    image: CompletionMessageBatchContentUnionMember2ImageMediaImage


CompletionMessageBatchContentUnionMember2: TypeAlias = Union[str, CompletionMessageBatchContentUnionMember2ImageMedia]

CompletionMessageBatchContent: TypeAlias = Union[
    str, CompletionMessageBatchContentImageMedia, List[CompletionMessageBatchContentUnionMember2]
]


class CompletionMessageBatchToolCall(BaseModel):
    arguments: Dict[
        str,
        Union[str, float, bool, List[Union[str, float, bool, None]], Dict[str, Union[str, float, bool, None]], None],
    ]

    call_id: str

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]


class CompletionMessageBatch(BaseModel):
    content: CompletionMessageBatchContent

    role: Literal["assistant"]

    stop_reason: Literal["end_of_turn", "end_of_message", "out_of_tokens"]

    tool_calls: List[CompletionMessageBatchToolCall]


class BatchInferenceCompletionResponse(BaseModel):
    completion_message_batch: List[CompletionMessageBatch]

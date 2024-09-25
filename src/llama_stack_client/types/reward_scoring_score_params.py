# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .shared_params.user_message import UserMessage
from .shared_params.system_message import SystemMessage
from .shared_params.completion_message import CompletionMessage
from .shared_params.tool_response_message import ToolResponseMessage

__all__ = [
    "RewardScoringScoreParams",
    "DialogGeneration",
    "DialogGenerationDialog",
    "DialogGenerationSampledGeneration",
]


class RewardScoringScoreParams(TypedDict, total=False):
    dialog_generations: Required[Iterable[DialogGeneration]]

    model: Required[str]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]


DialogGenerationDialog: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]

DialogGenerationSampledGeneration: TypeAlias = Union[UserMessage, SystemMessage, ToolResponseMessage, CompletionMessage]


class DialogGeneration(TypedDict, total=False):
    dialog: Required[Iterable[DialogGenerationDialog]]

    sampled_generations: Required[Iterable[DialogGenerationSampledGeneration]]

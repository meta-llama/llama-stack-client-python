# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.message import Message

__all__ = ["SyntheticDataGenerationGenerateParams"]


class SyntheticDataGenerationGenerateParams(TypedDict, total=False):
    dialogs: Required[Iterable[Message]]

    filtering_function: Required[Literal["none", "random", "top_k", "top_p", "top_k_top_p", "sigmoid"]]

    model: str

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]

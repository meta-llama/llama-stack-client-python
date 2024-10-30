# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScoringScoreBatchParams"]


class ScoringScoreBatchParams(TypedDict, total=False):
    dataset_id: Required[str]

    save_results_dataset: Required[bool]

    scoring_functions: Required[List[str]]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-ProviderData")]

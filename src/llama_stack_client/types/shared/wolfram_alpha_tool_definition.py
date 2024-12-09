# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .rest_api_execution_config import RestAPIExecutionConfig

__all__ = ["WolframAlphaToolDefinition"]


class WolframAlphaToolDefinition(BaseModel):
    api_key: str

    type: Literal["wolfram_alpha"]

    input_shields: Optional[List[str]] = None

    output_shields: Optional[List[str]] = None

    remote_execution: Optional[RestAPIExecutionConfig] = None

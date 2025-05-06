# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .param_type import ParamType
from .scoring_fn_params import ScoringFnParams

__all__ = ["ScoringFn"]


class ScoringFn(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    return_type: ParamType

    type: Literal["scoring_function"]

    description: Optional[str] = None

    params: Optional[ScoringFnParams] = None

    provider_resource_id: Optional[str] = None

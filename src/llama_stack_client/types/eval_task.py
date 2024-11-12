# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EvalTask"]


class EvalTask(BaseModel):
    dataset_id: str

    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    provider_resource_id: str

    scoring_functions: List[str]

    type: Literal["eval_task"]

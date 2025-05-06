# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .data_source import DataSource

__all__ = ["Dataset"]


class Dataset(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

    purpose: Literal["post-training/messages", "eval/question-answer", "eval/messages-answer"]
    """Purpose of the dataset. Each purpose has a required input data schema."""

    source: DataSource
    """A dataset that can be obtained from a URI."""

    type: Literal["dataset"]

    provider_resource_id: Optional[str] = None

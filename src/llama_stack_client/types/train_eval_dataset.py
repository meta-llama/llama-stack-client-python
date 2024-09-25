# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TrainEvalDataset"]


class TrainEvalDataset(BaseModel):
    columns: Dict[str, Literal["dialog", "text", "media", "number", "json"]]

    content_url: str

    metadata: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

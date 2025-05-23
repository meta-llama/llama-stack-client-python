# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Model"]


class Model(BaseModel):
    identifier: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    api_model_type: Literal["llm", "embedding"] = FieldInfo(alias="model_type")

    provider_id: str

    type: Literal["model"]

    provider_resource_id: Optional[str] = None

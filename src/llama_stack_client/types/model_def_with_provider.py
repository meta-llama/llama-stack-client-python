# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["ModelDefWithProvider"]


class ModelDefWithProvider(BaseModel):
    identifier: str

    llama_model: str

    metadata: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_id: str

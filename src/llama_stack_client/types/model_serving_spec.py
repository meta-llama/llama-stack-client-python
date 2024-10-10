# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union

from .._models import BaseModel

__all__ = ["ModelServingSpec", "ProviderConfig"]


class ProviderConfig(BaseModel):
    config: Dict[str, Union[bool, float, str, List[object], object, None]]

    provider_type: str


class ModelServingSpec(BaseModel):
    llama_model: object
    """
    The model family and SKU of the model along with other parameters corresponding
    to the model.
    """

    provider_config: ProviderConfig

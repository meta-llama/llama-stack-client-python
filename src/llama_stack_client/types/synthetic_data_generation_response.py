# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["SyntheticDataGenerationResponse"]


class SyntheticDataGenerationResponse(BaseModel):
    synthetic_data: List[Dict[str, Union[bool, float, str, List[object], object, None]]]

    statistics: Optional[Dict[str, Union[bool, float, str, List[object], object, None]]] = None

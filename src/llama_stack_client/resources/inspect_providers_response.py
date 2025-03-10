# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .provider_inspect_response import ProviderInspectResponse

__all__ = ["InspectProviderResponse"]


class InspectProviderResponse(BaseModel):
    data: ProviderInspectResponse

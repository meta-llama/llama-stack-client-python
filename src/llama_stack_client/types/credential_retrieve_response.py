# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CredentialRetrieveResponse"]


class CredentialRetrieveResponse(BaseModel):
    credential_id: str

    expires_at: datetime

    provider_id: str

    token_type: Literal["oauth2_authorization_code", "access_token"]
    """The type of credential token."""

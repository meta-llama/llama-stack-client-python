# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CredentialCreateParams"]


class CredentialCreateParams(TypedDict, total=False):
    token: Required[str]
    """The token itself."""

    provider_id: Required[str]
    """The ID of the provider to create credentials for."""

    token_type: Required[Literal["oauth2_authorization_code", "access_token"]]
    """The type of token to create.

    This is provided in the API to serve as lightweight documentation / metadata for
    the token.
    """

    ttl_seconds: Required[int]
    """The time to live for the credential in seconds.

    Defaults to 3600 seconds. When token_type is oauth2_authorization_code, the TTL
    is ignored and is obtained from the provider when exchanging the code for an
    access token.
    """

    nonce: str
    """The nonce is required when the token type is oauth2_authorization_code."""

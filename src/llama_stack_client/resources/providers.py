# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast, Dict, Any

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._wrappers import DataWrapper
from .._base_client import make_request_options
from ..types.provider_info import ProviderInfo
from ..types.provider_list_response import ProviderListResponse
from ..types import provider_update_params

__all__ = ["ProvidersResource", "AsyncProvidersResource"]


class ProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return ProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return ProvidersResourceWithStreamingResponse(self)
    
    def update(
        self,
        api: str,
        provider_id: str,
        provider_type: str,
        *,
        config: Dict[str, Any],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/v1/providers/{api}/{provider_id}/{provider_type}",
            body=maybe_transform(
                {
                    "config": config,
                },
                provider_update_params.UpdateProviderRequest,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderInfo,
        )

    def retrieve(
        self,
        provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderInfo:
        """
        Get detailed information about a specific provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._get(
            f"/v1/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderInfo,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """List all available providers."""
        return self._get(
            "/v1/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ProviderListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ProviderListResponse], DataWrapper[ProviderListResponse]),
        )


class AsyncProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/llamastack/llama-stack-client-python#with_streaming_response
        """
        return AsyncProvidersResourceWithStreamingResponse(self)
    

    async def update(
        self,
        api: str,
        provider_id: str,
        provider_type: str,
        *,
        config: Dict[str, Any],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderInfo:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/v1/providers/{api}/{provider_id}/{provider_type}",
            body=async_maybe_transform(
                {
                    "config": config,
                },
                provider_update_params.UpdateProviderRequest,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderInfo,
        )

    async def retrieve(
        self,
        provider_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderInfo:
        """
        Get detailed information about a specific provider.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._get(
            f"/v1/providers/{provider_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderInfo,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """List all available providers."""
        return await self._get(
            "/v1/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=DataWrapper[ProviderListResponse]._unwrapper,
            ),
            cast_to=cast(Type[ProviderListResponse], DataWrapper[ProviderListResponse]),
        )


class ProvidersResourceWithRawResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.update = to_raw_response_wrapper(
            providers.update,
        )
        self.retrieve = to_raw_response_wrapper(
            providers.retrieve,
        )
        self.list = to_raw_response_wrapper(
            providers.list,
        )


class AsyncProvidersResourceWithRawResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.update = async_to_raw_response_wrapper(
            providers.update,
        )
        self.retrieve = async_to_raw_response_wrapper(
            providers.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            providers.list,
        )


class ProvidersResourceWithStreamingResponse:
    def __init__(self, providers: ProvidersResource) -> None:
        self._providers = providers

        self.update = to_streamed_response_wrapper(
            providers.update,
        )
        self.retrieve = to_streamed_response_wrapper(
            providers.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            providers.list,
        )


class AsyncProvidersResourceWithStreamingResponse:
    def __init__(self, providers: AsyncProvidersResource) -> None:
        self._providers = providers

        self.update = async_to_streamed_response_wrapper(
            providers.update,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            providers.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            providers.list,
        )

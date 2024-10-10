# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import strip_not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.route_list_response import RouteListResponse

__all__ = ["RoutesResource", "AsyncRoutesResource"]


class RoutesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return RoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return RoutesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._get(
            "/routes/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteListResponse,
        )


class AsyncRoutesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncRoutesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/routes/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteListResponse,
        )


class RoutesResourceWithRawResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.list = to_raw_response_wrapper(
            routes.list,
        )


class AsyncRoutesResourceWithRawResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.list = async_to_raw_response_wrapper(
            routes.list,
        )


class RoutesResourceWithStreamingResponse:
    def __init__(self, routes: RoutesResource) -> None:
        self._routes = routes

        self.list = to_streamed_response_wrapper(
            routes.list,
        )


class AsyncRoutesResourceWithStreamingResponse:
    def __init__(self, routes: AsyncRoutesResource) -> None:
        self._routes = routes

        self.list = async_to_streamed_response_wrapper(
            routes.list,
        )

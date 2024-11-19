# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from ..types import shield_register_params, shield_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shield import Shield

__all__ = ["ShieldsResource", "AsyncShieldsResource"]


class ShieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return ShieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return ShieldsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        identifier: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Shield]:
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
            "/alpha/shields/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"identifier": identifier}, shield_retrieve_params.ShieldRetrieveParams),
            ),
            cast_to=Shield,
        )

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
    ) -> Shield:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._get(
            "/alpha/shields/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
        )

    def register(
        self,
        *,
        shield_id: str,
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        provider_shield_id: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Shield:
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
        return self._post(
            "/alpha/shields/register",
            body=maybe_transform(
                {
                    "shield_id": shield_id,
                    "params": params,
                    "provider_id": provider_id,
                    "provider_shield_id": provider_shield_id,
                },
                shield_register_params.ShieldRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
        )


class AsyncShieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncShieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncShieldsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        identifier: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[Shield]:
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
            "/alpha/shields/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"identifier": identifier}, shield_retrieve_params.ShieldRetrieveParams
                ),
            ),
            cast_to=Shield,
        )

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
    ) -> Shield:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/alpha/shields/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
        )

    async def register(
        self,
        *,
        shield_id: str,
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
        provider_shield_id: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Shield:
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
        return await self._post(
            "/alpha/shields/register",
            body=await async_maybe_transform(
                {
                    "shield_id": shield_id,
                    "params": params,
                    "provider_id": provider_id,
                    "provider_shield_id": provider_shield_id,
                },
                shield_register_params.ShieldRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Shield,
        )


class ShieldsResourceWithRawResponse:
    def __init__(self, shields: ShieldsResource) -> None:
        self._shields = shields

        self.retrieve = to_raw_response_wrapper(
            shields.retrieve,
        )
        self.list = to_raw_response_wrapper(
            shields.list,
        )
        self.register = to_raw_response_wrapper(
            shields.register,
        )


class AsyncShieldsResourceWithRawResponse:
    def __init__(self, shields: AsyncShieldsResource) -> None:
        self._shields = shields

        self.retrieve = async_to_raw_response_wrapper(
            shields.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            shields.list,
        )
        self.register = async_to_raw_response_wrapper(
            shields.register,
        )


class ShieldsResourceWithStreamingResponse:
    def __init__(self, shields: ShieldsResource) -> None:
        self._shields = shields

        self.retrieve = to_streamed_response_wrapper(
            shields.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            shields.list,
        )
        self.register = to_streamed_response_wrapper(
            shields.register,
        )


class AsyncShieldsResourceWithStreamingResponse:
    def __init__(self, shields: AsyncShieldsResource) -> None:
        self._shields = shields

        self.retrieve = async_to_streamed_response_wrapper(
            shields.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            shields.list,
        )
        self.register = async_to_streamed_response_wrapper(
            shields.register,
        )

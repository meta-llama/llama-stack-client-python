# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ..types import safety_run_shield_params
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
from ..types.run_shield_response import RunShieldResponse

__all__ = ["SafetyResource", "AsyncSafetyResource"]


class SafetyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SafetyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return SafetyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SafetyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return SafetyResourceWithStreamingResponse(self)

    def run_shield(
        self,
        *,
        messages: Iterable[safety_run_shield_params.Message],
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        shield_type: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunShieldResponse:
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
            "/safety/run_shield",
            body=maybe_transform(
                {
                    "messages": messages,
                    "params": params,
                    "shield_type": shield_type,
                },
                safety_run_shield_params.SafetyRunShieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunShieldResponse,
        )


class AsyncSafetyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSafetyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSafetyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSafetyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncSafetyResourceWithStreamingResponse(self)

    async def run_shield(
        self,
        *,
        messages: Iterable[safety_run_shield_params.Message],
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        shield_type: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RunShieldResponse:
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
            "/safety/run_shield",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "params": params,
                    "shield_type": shield_type,
                },
                safety_run_shield_params.SafetyRunShieldParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunShieldResponse,
        )


class SafetyResourceWithRawResponse:
    def __init__(self, safety: SafetyResource) -> None:
        self._safety = safety

        self.run_shield = to_raw_response_wrapper(
            safety.run_shield,
        )


class AsyncSafetyResourceWithRawResponse:
    def __init__(self, safety: AsyncSafetyResource) -> None:
        self._safety = safety

        self.run_shield = async_to_raw_response_wrapper(
            safety.run_shield,
        )


class SafetyResourceWithStreamingResponse:
    def __init__(self, safety: SafetyResource) -> None:
        self._safety = safety

        self.run_shield = to_streamed_response_wrapper(
            safety.run_shield,
        )


class AsyncSafetyResourceWithStreamingResponse:
    def __init__(self, safety: AsyncSafetyResource) -> None:
        self._safety = safety

        self.run_shield = async_to_streamed_response_wrapper(
            safety.run_shield,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import telemetry_get_trace_params, telemetry_log_event_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.trace import Trace
from .._base_client import make_request_options

__all__ = ["TelemetryResource", "AsyncTelemetryResource"]


class TelemetryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return TelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return TelemetryResourceWithStreamingResponse(self)

    def get_trace(
        self,
        *,
        trace_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Trace:
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
            "/telemetry/get_trace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"trace_id": trace_id}, telemetry_get_trace_params.TelemetryGetTraceParams),
            ),
            cast_to=Trace,
        )

    def log_event(
        self,
        *,
        event: telemetry_log_event_params.Event,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._post(
            "/telemetry/log_event",
            body=maybe_transform({"event": event}, telemetry_log_event_params.TelemetryLogEventParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTelemetryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTelemetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTelemetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTelemetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncTelemetryResourceWithStreamingResponse(self)

    async def get_trace(
        self,
        *,
        trace_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Trace:
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
            "/telemetry/get_trace",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"trace_id": trace_id}, telemetry_get_trace_params.TelemetryGetTraceParams
                ),
            ),
            cast_to=Trace,
        )

    async def log_event(
        self,
        *,
        event: telemetry_log_event_params.Event,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/telemetry/log_event",
            body=await async_maybe_transform({"event": event}, telemetry_log_event_params.TelemetryLogEventParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TelemetryResourceWithRawResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_trace = to_raw_response_wrapper(
            telemetry.get_trace,
        )
        self.log_event = to_raw_response_wrapper(
            telemetry.log_event,
        )


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_trace = async_to_raw_response_wrapper(
            telemetry.get_trace,
        )
        self.log_event = async_to_raw_response_wrapper(
            telemetry.log_event,
        )


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_trace = to_streamed_response_wrapper(
            telemetry.get_trace,
        )
        self.log_event = to_streamed_response_wrapper(
            telemetry.log_event,
        )


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_trace = async_to_streamed_response_wrapper(
            telemetry.get_trace,
        )
        self.log_event = async_to_streamed_response_wrapper(
            telemetry.log_event,
        )

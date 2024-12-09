# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable

import httpx

from ..types import (
    telemetry_log_event_params,
    telemetry_query_spans_params,
    telemetry_query_traces_params,
    telemetry_get_span_tree_params,
    telemetry_save_spans_to_dataset_params,
)
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
from ..types.span_with_children import SpanWithChildren
from ..types.telemetry_query_spans_response import TelemetryQuerySpansResponse

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

    def get_span_tree(
        self,
        *,
        span_id: str,
        max_depth: int | NotGiven = NOT_GIVEN,
        attributes_to_return: List[str] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanWithChildren:
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
            "/alpha/telemetry/get-span-tree",
            body=maybe_transform(
                {"attributes_to_return": attributes_to_return},
                telemetry_get_span_tree_params.TelemetryGetSpanTreeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "span_id": span_id,
                        "max_depth": max_depth,
                    },
                    telemetry_get_span_tree_params.TelemetryGetSpanTreeParams,
                ),
            ),
            cast_to=SpanWithChildren,
        )

    def log_event(
        self,
        *,
        event: telemetry_log_event_params.Event,
        ttl_seconds: int,
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
            "/alpha/telemetry/log-event",
            body=maybe_transform(
                {
                    "event": event,
                    "ttl_seconds": ttl_seconds,
                },
                telemetry_log_event_params.TelemetryLogEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query_spans(
        self,
        *,
        attribute_filters: Iterable[telemetry_query_spans_params.AttributeFilter],
        attributes_to_return: List[str],
        max_depth: int | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelemetryQuerySpansResponse:
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
        return self._post(
            "/alpha/telemetry/query-spans",
            body=maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                telemetry_query_spans_params.TelemetryQuerySpansParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelemetryQuerySpansResponse,
        )

    def query_traces(
        self,
        *,
        attribute_filters: Iterable[telemetry_query_traces_params.AttributeFilter] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: List[str] | NotGiven = NOT_GIVEN,
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
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._post(
            "/alpha/telemetry/query-traces",
            body=maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "limit": limit,
                    "offset": offset,
                    "order_by": order_by,
                },
                telemetry_query_traces_params.TelemetryQueryTracesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Trace,
        )

    def save_spans_to_dataset(
        self,
        *,
        attribute_filters: Iterable[telemetry_save_spans_to_dataset_params.AttributeFilter],
        attributes_to_save: List[str],
        dataset_id: str,
        max_depth: int | NotGiven = NOT_GIVEN,
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
            "/alpha/telemetry/save-spans-to-dataset",
            body=maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_save": attributes_to_save,
                    "dataset_id": dataset_id,
                    "max_depth": max_depth,
                },
                telemetry_save_spans_to_dataset_params.TelemetrySaveSpansToDatasetParams,
            ),
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

    async def get_span_tree(
        self,
        *,
        span_id: str,
        max_depth: int | NotGiven = NOT_GIVEN,
        attributes_to_return: List[str] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SpanWithChildren:
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
            "/alpha/telemetry/get-span-tree",
            body=await async_maybe_transform(
                {"attributes_to_return": attributes_to_return},
                telemetry_get_span_tree_params.TelemetryGetSpanTreeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "span_id": span_id,
                        "max_depth": max_depth,
                    },
                    telemetry_get_span_tree_params.TelemetryGetSpanTreeParams,
                ),
            ),
            cast_to=SpanWithChildren,
        )

    async def log_event(
        self,
        *,
        event: telemetry_log_event_params.Event,
        ttl_seconds: int,
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
            "/alpha/telemetry/log-event",
            body=await async_maybe_transform(
                {
                    "event": event,
                    "ttl_seconds": ttl_seconds,
                },
                telemetry_log_event_params.TelemetryLogEventParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query_spans(
        self,
        *,
        attribute_filters: Iterable[telemetry_query_spans_params.AttributeFilter],
        attributes_to_return: List[str],
        max_depth: int | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TelemetryQuerySpansResponse:
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
        return await self._post(
            "/alpha/telemetry/query-spans",
            body=await async_maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_return": attributes_to_return,
                    "max_depth": max_depth,
                },
                telemetry_query_spans_params.TelemetryQuerySpansParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TelemetryQuerySpansResponse,
        )

    async def query_traces(
        self,
        *,
        attribute_filters: Iterable[telemetry_query_traces_params.AttributeFilter] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        order_by: List[str] | NotGiven = NOT_GIVEN,
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
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/alpha/telemetry/query-traces",
            body=await async_maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "limit": limit,
                    "offset": offset,
                    "order_by": order_by,
                },
                telemetry_query_traces_params.TelemetryQueryTracesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Trace,
        )

    async def save_spans_to_dataset(
        self,
        *,
        attribute_filters: Iterable[telemetry_save_spans_to_dataset_params.AttributeFilter],
        attributes_to_save: List[str],
        dataset_id: str,
        max_depth: int | NotGiven = NOT_GIVEN,
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
            "/alpha/telemetry/save-spans-to-dataset",
            body=await async_maybe_transform(
                {
                    "attribute_filters": attribute_filters,
                    "attributes_to_save": attributes_to_save,
                    "dataset_id": dataset_id,
                    "max_depth": max_depth,
                },
                telemetry_save_spans_to_dataset_params.TelemetrySaveSpansToDatasetParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TelemetryResourceWithRawResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_span_tree = to_raw_response_wrapper(
            telemetry.get_span_tree,
        )
        self.log_event = to_raw_response_wrapper(
            telemetry.log_event,
        )
        self.query_spans = to_raw_response_wrapper(
            telemetry.query_spans,
        )
        self.query_traces = to_raw_response_wrapper(
            telemetry.query_traces,
        )
        self.save_spans_to_dataset = to_raw_response_wrapper(
            telemetry.save_spans_to_dataset,
        )


class AsyncTelemetryResourceWithRawResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_span_tree = async_to_raw_response_wrapper(
            telemetry.get_span_tree,
        )
        self.log_event = async_to_raw_response_wrapper(
            telemetry.log_event,
        )
        self.query_spans = async_to_raw_response_wrapper(
            telemetry.query_spans,
        )
        self.query_traces = async_to_raw_response_wrapper(
            telemetry.query_traces,
        )
        self.save_spans_to_dataset = async_to_raw_response_wrapper(
            telemetry.save_spans_to_dataset,
        )


class TelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: TelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_span_tree = to_streamed_response_wrapper(
            telemetry.get_span_tree,
        )
        self.log_event = to_streamed_response_wrapper(
            telemetry.log_event,
        )
        self.query_spans = to_streamed_response_wrapper(
            telemetry.query_spans,
        )
        self.query_traces = to_streamed_response_wrapper(
            telemetry.query_traces,
        )
        self.save_spans_to_dataset = to_streamed_response_wrapper(
            telemetry.save_spans_to_dataset,
        )


class AsyncTelemetryResourceWithStreamingResponse:
    def __init__(self, telemetry: AsyncTelemetryResource) -> None:
        self._telemetry = telemetry

        self.get_span_tree = async_to_streamed_response_wrapper(
            telemetry.get_span_tree,
        )
        self.log_event = async_to_streamed_response_wrapper(
            telemetry.log_event,
        )
        self.query_spans = async_to_streamed_response_wrapper(
            telemetry.query_spans,
        )
        self.query_traces = async_to_streamed_response_wrapper(
            telemetry.query_traces,
        )
        self.save_spans_to_dataset = async_to_streamed_response_wrapper(
            telemetry.save_spans_to_dataset,
        )

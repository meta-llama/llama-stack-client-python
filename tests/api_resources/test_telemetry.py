# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    Trace,
    SpanWithChildren,
    TelemetryQuerySpansResponse,
)
from llama_stack_client._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelemetry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_span_tree(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.get_span_tree(
            span_id="span_id",
        )
        assert_matches_type(SpanWithChildren, telemetry, path=["response"])

    @parametrize
    def test_method_get_span_tree_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.get_span_tree(
            span_id="span_id",
            max_depth=0,
            attributes_to_return=["string"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(SpanWithChildren, telemetry, path=["response"])

    @parametrize
    def test_raw_response_get_span_tree(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.get_span_tree(
            span_id="span_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(SpanWithChildren, telemetry, path=["response"])

    @parametrize
    def test_streaming_response_get_span_tree(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.get_span_tree(
            span_id="span_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(SpanWithChildren, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_log_event(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.log_event(
            event={
                "message": "message",
                "severity": "verbose",
                "span_id": "span_id",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "trace_id": "trace_id",
                "type": "unstructured_log",
            },
            ttl_seconds=0,
        )
        assert telemetry is None

    @parametrize
    def test_method_log_event_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.log_event(
            event={
                "message": "message",
                "severity": "verbose",
                "span_id": "span_id",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "trace_id": "trace_id",
                "type": "unstructured_log",
                "attributes": {"foo": True},
            },
            ttl_seconds=0,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert telemetry is None

    @parametrize
    def test_raw_response_log_event(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.log_event(
            event={
                "message": "message",
                "severity": "verbose",
                "span_id": "span_id",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "trace_id": "trace_id",
                "type": "unstructured_log",
            },
            ttl_seconds=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert telemetry is None

    @parametrize
    def test_streaming_response_log_event(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.log_event(
            event={
                "message": "message",
                "severity": "verbose",
                "span_id": "span_id",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "trace_id": "trace_id",
                "type": "unstructured_log",
            },
            ttl_seconds=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert telemetry is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_query_spans(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_query_spans_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
            max_depth=0,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_query_spans(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_query_spans(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_query_traces(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_traces()
        assert_matches_type(Trace, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_query_traces_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.query_traces(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            limit=0,
            offset=0,
            order_by=["string"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Trace, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_query_traces(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.query_traces()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(Trace, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_query_traces(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.query_traces() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(Trace, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_save_spans_to_dataset(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.save_spans_to_dataset(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        )
        assert telemetry is None

    @parametrize
    def test_method_save_spans_to_dataset_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.save_spans_to_dataset(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
            max_depth=0,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert telemetry is None

    @parametrize
    def test_raw_response_save_spans_to_dataset(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.save_spans_to_dataset(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert telemetry is None

    @parametrize
    def test_streaming_response_save_spans_to_dataset(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.save_spans_to_dataset(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert telemetry is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTelemetry:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_span_tree(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.get_span_tree(
            span_id="span_id",
        )
        assert_matches_type(SpanWithChildren, telemetry, path=["response"])

    @parametrize
    async def test_method_get_span_tree_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.get_span_tree(
            span_id="span_id",
            max_depth=0,
            attributes_to_return=["string"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(SpanWithChildren, telemetry, path=["response"])

    @parametrize
    async def test_raw_response_get_span_tree(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.get_span_tree(
            span_id="span_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(SpanWithChildren, telemetry, path=["response"])

    @parametrize
    async def test_streaming_response_get_span_tree(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.get_span_tree(
            span_id="span_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(SpanWithChildren, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_log_event(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.log_event(
            event={
                "message": "message",
                "severity": "verbose",
                "span_id": "span_id",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "trace_id": "trace_id",
                "type": "unstructured_log",
            },
            ttl_seconds=0,
        )
        assert telemetry is None

    @parametrize
    async def test_method_log_event_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.log_event(
            event={
                "message": "message",
                "severity": "verbose",
                "span_id": "span_id",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "trace_id": "trace_id",
                "type": "unstructured_log",
                "attributes": {"foo": True},
            },
            ttl_seconds=0,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert telemetry is None

    @parametrize
    async def test_raw_response_log_event(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.log_event(
            event={
                "message": "message",
                "severity": "verbose",
                "span_id": "span_id",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "trace_id": "trace_id",
                "type": "unstructured_log",
            },
            ttl_seconds=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert telemetry is None

    @parametrize
    async def test_streaming_response_log_event(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.log_event(
            event={
                "message": "message",
                "severity": "verbose",
                "span_id": "span_id",
                "timestamp": parse_datetime("2019-12-27T18:11:19.117Z"),
                "trace_id": "trace_id",
                "type": "unstructured_log",
            },
            ttl_seconds=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert telemetry is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_query_spans(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_query_spans_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
            max_depth=0,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_query_spans(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_query_spans(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.query_spans(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_return=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(TelemetryQuerySpansResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_query_traces(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_traces()
        assert_matches_type(Trace, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_query_traces_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.query_traces(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            limit=0,
            offset=0,
            order_by=["string"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Trace, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_query_traces(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.query_traces()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(Trace, telemetry, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_query_traces(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.query_traces() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(Trace, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_save_spans_to_dataset(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.save_spans_to_dataset(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        )
        assert telemetry is None

    @parametrize
    async def test_method_save_spans_to_dataset_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.save_spans_to_dataset(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
            max_depth=0,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert telemetry is None

    @parametrize
    async def test_raw_response_save_spans_to_dataset(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.save_spans_to_dataset(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert telemetry is None

    @parametrize
    async def test_streaming_response_save_spans_to_dataset(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.save_spans_to_dataset(
            attribute_filters=[
                {
                    "key": "key",
                    "op": "eq",
                    "value": True,
                }
            ],
            attributes_to_save=["string"],
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert telemetry is None

        assert cast(Any, response.is_closed) is True

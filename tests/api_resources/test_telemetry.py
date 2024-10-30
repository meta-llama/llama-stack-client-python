# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import Trace
from llama_stack_client._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelemetry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_trace(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.get_trace(
            trace_id="trace_id",
        )
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    def test_method_get_trace_with_all_params(self, client: LlamaStackClient) -> None:
        telemetry = client.telemetry.get_trace(
            trace_id="trace_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    def test_raw_response_get_trace(self, client: LlamaStackClient) -> None:
        response = client.telemetry.with_raw_response.get_trace(
            trace_id="trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    def test_streaming_response_get_trace(self, client: LlamaStackClient) -> None:
        with client.telemetry.with_streaming_response.get_trace(
            trace_id="trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(Trace, telemetry, path=["response"])

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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert telemetry is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTelemetry:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_trace(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.get_trace(
            trace_id="trace_id",
        )
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    async def test_method_get_trace_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        telemetry = await async_client.telemetry.get_trace(
            trace_id="trace_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    async def test_raw_response_get_trace(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.telemetry.with_raw_response.get_trace(
            trace_id="trace_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(Trace, telemetry, path=["response"])

    @parametrize
    async def test_streaming_response_get_trace(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.telemetry.with_streaming_response.get_trace(
            trace_id="trace_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(Trace, telemetry, path=["response"])

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
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert telemetry is None

        assert cast(Any, response.is_closed) is True

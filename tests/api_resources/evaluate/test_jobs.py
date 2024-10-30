# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.evaluate import (
    JobStatus,
    EvaluateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_cancel(self, client: LlamaStackClient) -> None:
        job = client.evaluate.jobs.cancel(
            job_id="job_id",
        )
        assert job is None

    @parametrize
    def test_method_cancel_with_all_params(self, client: LlamaStackClient) -> None:
        job = client.evaluate.jobs.cancel(
            job_id="job_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert job is None

    @parametrize
    def test_raw_response_cancel(self, client: LlamaStackClient) -> None:
        response = client.evaluate.jobs.with_raw_response.cancel(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @parametrize
    def test_streaming_response_cancel(self, client: LlamaStackClient) -> None:
        with client.evaluate.jobs.with_streaming_response.cancel(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_result(self, client: LlamaStackClient) -> None:
        job = client.evaluate.jobs.result(
            job_id="job_id",
        )
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    def test_method_result_with_all_params(self, client: LlamaStackClient) -> None:
        job = client.evaluate.jobs.result(
            job_id="job_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    def test_raw_response_result(self, client: LlamaStackClient) -> None:
        response = client.evaluate.jobs.with_raw_response.result(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    def test_streaming_response_result(self, client: LlamaStackClient) -> None:
        with client.evaluate.jobs.with_streaming_response.result(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(EvaluateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_status(self, client: LlamaStackClient) -> None:
        job = client.evaluate.jobs.status(
            job_id="job_id",
        )
        assert_matches_type(Optional[JobStatus], job, path=["response"])

    @parametrize
    def test_method_status_with_all_params(self, client: LlamaStackClient) -> None:
        job = client.evaluate.jobs.status(
            job_id="job_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[JobStatus], job, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: LlamaStackClient) -> None:
        response = client.evaluate.jobs.with_raw_response.status(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[JobStatus], job, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: LlamaStackClient) -> None:
        with client.evaluate.jobs.with_streaming_response.status(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[JobStatus], job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.evaluate.jobs.cancel(
            job_id="job_id",
        )
        assert job is None

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.evaluate.jobs.cancel(
            job_id="job_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert job is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.evaluate.jobs.with_raw_response.cancel(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.evaluate.jobs.with_streaming_response.cancel(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_result(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.evaluate.jobs.result(
            job_id="job_id",
        )
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    async def test_method_result_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.evaluate.jobs.result(
            job_id="job_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    async def test_raw_response_result(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.evaluate.jobs.with_raw_response.result(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(EvaluateResponse, job, path=["response"])

    @parametrize
    async def test_streaming_response_result(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.evaluate.jobs.with_streaming_response.result(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(EvaluateResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_status(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.evaluate.jobs.status(
            job_id="job_id",
        )
        assert_matches_type(Optional[JobStatus], job, path=["response"])

    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.evaluate.jobs.status(
            job_id="job_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[JobStatus], job, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.evaluate.jobs.with_raw_response.status(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[JobStatus], job, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.evaluate.jobs.with_streaming_response.status(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[JobStatus], job, path=["response"])

        assert cast(Any, response.is_closed) is True

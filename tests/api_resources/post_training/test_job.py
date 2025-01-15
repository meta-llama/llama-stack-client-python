# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import PostTrainingJob
from llama_stack_client.types.post_training import (
    JobStatusResponse,
    JobArtifactsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJob:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.list()
        assert_matches_type(PostTrainingJob, job, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(PostTrainingJob, job, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.post_training.job.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(PostTrainingJob, job, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.post_training.job.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(PostTrainingJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_artifacts(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.artifacts(
            job_uuid="job_uuid",
        )
        assert_matches_type(Optional[JobArtifactsResponse], job, path=["response"])

    @parametrize
    def test_method_artifacts_with_all_params(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.artifacts(
            job_uuid="job_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[JobArtifactsResponse], job, path=["response"])

    @parametrize
    def test_raw_response_artifacts(self, client: LlamaStackClient) -> None:
        response = client.post_training.job.with_raw_response.artifacts(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[JobArtifactsResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_artifacts(self, client: LlamaStackClient) -> None:
        with client.post_training.job.with_streaming_response.artifacts(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[JobArtifactsResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_cancel(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.cancel(
            job_uuid="job_uuid",
        )
        assert job is None

    @parametrize
    def test_method_cancel_with_all_params(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.cancel(
            job_uuid="job_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert job is None

    @parametrize
    def test_raw_response_cancel(self, client: LlamaStackClient) -> None:
        response = client.post_training.job.with_raw_response.cancel(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert job is None

    @parametrize
    def test_streaming_response_cancel(self, client: LlamaStackClient) -> None:
        with client.post_training.job.with_streaming_response.cancel(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_status(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.status(
            job_uuid="job_uuid",
        )
        assert_matches_type(Optional[JobStatusResponse], job, path=["response"])

    @parametrize
    def test_method_status_with_all_params(self, client: LlamaStackClient) -> None:
        job = client.post_training.job.status(
            job_uuid="job_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[JobStatusResponse], job, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: LlamaStackClient) -> None:
        response = client.post_training.job.with_raw_response.status(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Optional[JobStatusResponse], job, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: LlamaStackClient) -> None:
        with client.post_training.job.with_streaming_response.status(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Optional[JobStatusResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncJob:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.list()
        assert_matches_type(PostTrainingJob, job, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(PostTrainingJob, job, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.job.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(PostTrainingJob, job, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.job.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(PostTrainingJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_artifacts(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.artifacts(
            job_uuid="job_uuid",
        )
        assert_matches_type(Optional[JobArtifactsResponse], job, path=["response"])

    @parametrize
    async def test_method_artifacts_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.artifacts(
            job_uuid="job_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[JobArtifactsResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_artifacts(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.job.with_raw_response.artifacts(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[JobArtifactsResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_artifacts(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.job.with_streaming_response.artifacts(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[JobArtifactsResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.cancel(
            job_uuid="job_uuid",
        )
        assert job is None

    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.cancel(
            job_uuid="job_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert job is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.job.with_raw_response.cancel(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert job is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.job.with_streaming_response.cancel(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert job is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_status(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.status(
            job_uuid="job_uuid",
        )
        assert_matches_type(Optional[JobStatusResponse], job, path=["response"])

    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        job = await async_client.post_training.job.status(
            job_uuid="job_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[JobStatusResponse], job, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.post_training.job.with_raw_response.status(
            job_uuid="job_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Optional[JobStatusResponse], job, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.post_training.job.with_streaming_response.status(
            job_uuid="job_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Optional[JobStatusResponse], job, path=["response"])

        assert cast(Any, response.is_closed) is True

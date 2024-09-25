# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import TrainEvalDataset

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.create(
            dataset={
                "columns": {"foo": "dialog"},
                "content_url": "https://example.com",
            },
            uuid="uuid",
        )
        assert dataset is None

    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.create(
            dataset={
                "columns": {"foo": "dialog"},
                "content_url": "https://example.com",
                "metadata": {"foo": True},
            },
            uuid="uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.datasets.with_raw_response.create(
            dataset={
                "columns": {"foo": "dialog"},
                "content_url": "https://example.com",
            },
            uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.datasets.with_streaming_response.create(
            dataset={
                "columns": {"foo": "dialog"},
                "content_url": "https://example.com",
            },
            uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.delete(
            dataset_uuid="dataset_uuid",
        )
        assert dataset is None

    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.delete(
            dataset_uuid="dataset_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_delete(self, client: LlamaStackClient) -> None:
        response = client.datasets.with_raw_response.delete(
            dataset_uuid="dataset_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_delete(self, client: LlamaStackClient) -> None:
        with client.datasets.with_streaming_response.delete(
            dataset_uuid="dataset_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.get(
            dataset_uuid="dataset_uuid",
        )
        assert_matches_type(TrainEvalDataset, dataset, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.get(
            dataset_uuid="dataset_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(TrainEvalDataset, dataset, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LlamaStackClient) -> None:
        response = client.datasets.with_raw_response.get(
            dataset_uuid="dataset_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(TrainEvalDataset, dataset, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LlamaStackClient) -> None:
        with client.datasets.with_streaming_response.get(
            dataset_uuid="dataset_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(TrainEvalDataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.create(
            dataset={
                "columns": {"foo": "dialog"},
                "content_url": "https://example.com",
            },
            uuid="uuid",
        )
        assert dataset is None

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.create(
            dataset={
                "columns": {"foo": "dialog"},
                "content_url": "https://example.com",
                "metadata": {"foo": True},
            },
            uuid="uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasets.with_raw_response.create(
            dataset={
                "columns": {"foo": "dialog"},
                "content_url": "https://example.com",
            },
            uuid="uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasets.with_streaming_response.create(
            dataset={
                "columns": {"foo": "dialog"},
                "content_url": "https://example.com",
            },
            uuid="uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.delete(
            dataset_uuid="dataset_uuid",
        )
        assert dataset is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.delete(
            dataset_uuid="dataset_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasets.with_raw_response.delete(
            dataset_uuid="dataset_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasets.with_streaming_response.delete(
            dataset_uuid="dataset_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.get(
            dataset_uuid="dataset_uuid",
        )
        assert_matches_type(TrainEvalDataset, dataset, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.get(
            dataset_uuid="dataset_uuid",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(TrainEvalDataset, dataset, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasets.with_raw_response.get(
            dataset_uuid="dataset_uuid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(TrainEvalDataset, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasets.with_streaming_response.get(
            dataset_uuid="dataset_uuid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(TrainEvalDataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

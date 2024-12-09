# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    DatasetListResponse,
    DatasetRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.retrieve(
            dataset_id="dataset_id",
        )
        assert_matches_type(Optional[DatasetRetrieveResponse], dataset, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.retrieve(
            dataset_id="dataset_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[DatasetRetrieveResponse], dataset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.datasets.with_raw_response.retrieve(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Optional[DatasetRetrieveResponse], dataset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.datasets.with_streaming_response.retrieve(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Optional[DatasetRetrieveResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.register(
            dataset_id="dataset_id",
            dataset_schema={"foo": {"type": "string"}},
            url="https://example.com",
        )
        assert dataset is None

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.register(
            dataset_id="dataset_id",
            dataset_schema={"foo": {"type": "string"}},
            url="https://example.com",
            metadata={"foo": True},
            provider_dataset_id="provider_dataset_id",
            provider_id="provider_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        response = client.datasets.with_raw_response.register(
            dataset_id="dataset_id",
            dataset_schema={"foo": {"type": "string"}},
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with client.datasets.with_streaming_response.register(
            dataset_id="dataset_id",
            dataset_schema={"foo": {"type": "string"}},
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unregister(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.unregister(
            dataset_id="dataset_id",
        )
        assert dataset is None

    @parametrize
    def test_method_unregister_with_all_params(self, client: LlamaStackClient) -> None:
        dataset = client.datasets.unregister(
            dataset_id="dataset_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_unregister(self, client: LlamaStackClient) -> None:
        response = client.datasets.with_raw_response.unregister(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_unregister(self, client: LlamaStackClient) -> None:
        with client.datasets.with_streaming_response.unregister(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.retrieve(
            dataset_id="dataset_id",
        )
        assert_matches_type(Optional[DatasetRetrieveResponse], dataset, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.retrieve(
            dataset_id="dataset_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[DatasetRetrieveResponse], dataset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasets.with_raw_response.retrieve(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Optional[DatasetRetrieveResponse], dataset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasets.with_streaming_response.retrieve(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Optional[DatasetRetrieveResponse], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.register(
            dataset_id="dataset_id",
            dataset_schema={"foo": {"type": "string"}},
            url="https://example.com",
        )
        assert dataset is None

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.register(
            dataset_id="dataset_id",
            dataset_schema={"foo": {"type": "string"}},
            url="https://example.com",
            metadata={"foo": True},
            provider_dataset_id="provider_dataset_id",
            provider_id="provider_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasets.with_raw_response.register(
            dataset_id="dataset_id",
            dataset_schema={"foo": {"type": "string"}},
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasets.with_streaming_response.register(
            dataset_id="dataset_id",
            dataset_schema={"foo": {"type": "string"}},
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.unregister(
            dataset_id="dataset_id",
        )
        assert dataset is None

    @parametrize
    async def test_method_unregister_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        dataset = await async_client.datasets.unregister(
            dataset_id="dataset_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasets.with_raw_response.unregister(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasets.with_streaming_response.unregister(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

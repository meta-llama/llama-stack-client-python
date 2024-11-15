# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    MemoryBankListResponse,
    MemoryBankRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemoryBanks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        memory_bank = client.memory_banks.retrieve(
            memory_bank_id="memory_bank_id",
        )
        assert_matches_type(Optional[MemoryBankRetrieveResponse], memory_bank, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        memory_bank = client.memory_banks.retrieve(
            memory_bank_id="memory_bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[MemoryBankRetrieveResponse], memory_bank, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.memory_banks.with_raw_response.retrieve(
            memory_bank_id="memory_bank_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_bank = response.parse()
        assert_matches_type(Optional[MemoryBankRetrieveResponse], memory_bank, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.memory_banks.with_streaming_response.retrieve(
            memory_bank_id="memory_bank_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_bank = response.parse()
            assert_matches_type(Optional[MemoryBankRetrieveResponse], memory_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        memory_bank = client.memory_banks.list()
        assert_matches_type(MemoryBankListResponse, memory_bank, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        memory_bank = client.memory_banks.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(MemoryBankListResponse, memory_bank, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.memory_banks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_bank = response.parse()
        assert_matches_type(MemoryBankListResponse, memory_bank, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.memory_banks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_bank = response.parse()
            assert_matches_type(MemoryBankListResponse, memory_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        memory_bank = client.memory_banks.register(
            memory_bank_id="memory_bank_id",
            params={
                "chunk_size_in_tokens": 0,
                "embedding_model": "embedding_model",
                "memory_bank_type": "vector",
            },
        )
        assert memory_bank is None

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        memory_bank = client.memory_banks.register(
            memory_bank_id="memory_bank_id",
            params={
                "chunk_size_in_tokens": 0,
                "embedding_model": "embedding_model",
                "memory_bank_type": "vector",
                "overlap_size_in_tokens": 0,
            },
            provider_id="provider_id",
            provider_memory_bank_id="provider_memory_bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert memory_bank is None

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        response = client.memory_banks.with_raw_response.register(
            memory_bank_id="memory_bank_id",
            params={
                "chunk_size_in_tokens": 0,
                "embedding_model": "embedding_model",
                "memory_bank_type": "vector",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_bank = response.parse()
        assert memory_bank is None

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with client.memory_banks.with_streaming_response.register(
            memory_bank_id="memory_bank_id",
            params={
                "chunk_size_in_tokens": 0,
                "embedding_model": "embedding_model",
                "memory_bank_type": "vector",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_bank = response.parse()
            assert memory_bank is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unregister(self, client: LlamaStackClient) -> None:
        memory_bank = client.memory_banks.unregister(
            memory_bank_id="memory_bank_id",
        )
        assert memory_bank is None

    @parametrize
    def test_method_unregister_with_all_params(self, client: LlamaStackClient) -> None:
        memory_bank = client.memory_banks.unregister(
            memory_bank_id="memory_bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert memory_bank is None

    @parametrize
    def test_raw_response_unregister(self, client: LlamaStackClient) -> None:
        response = client.memory_banks.with_raw_response.unregister(
            memory_bank_id="memory_bank_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_bank = response.parse()
        assert memory_bank is None

    @parametrize
    def test_streaming_response_unregister(self, client: LlamaStackClient) -> None:
        with client.memory_banks.with_streaming_response.unregister(
            memory_bank_id="memory_bank_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_bank = response.parse()
            assert memory_bank is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMemoryBanks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        memory_bank = await async_client.memory_banks.retrieve(
            memory_bank_id="memory_bank_id",
        )
        assert_matches_type(Optional[MemoryBankRetrieveResponse], memory_bank, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory_bank = await async_client.memory_banks.retrieve(
            memory_bank_id="memory_bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[MemoryBankRetrieveResponse], memory_bank, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory_banks.with_raw_response.retrieve(
            memory_bank_id="memory_bank_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_bank = await response.parse()
        assert_matches_type(Optional[MemoryBankRetrieveResponse], memory_bank, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory_banks.with_streaming_response.retrieve(
            memory_bank_id="memory_bank_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_bank = await response.parse()
            assert_matches_type(Optional[MemoryBankRetrieveResponse], memory_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        memory_bank = await async_client.memory_banks.list()
        assert_matches_type(MemoryBankListResponse, memory_bank, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory_bank = await async_client.memory_banks.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(MemoryBankListResponse, memory_bank, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory_banks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_bank = await response.parse()
        assert_matches_type(MemoryBankListResponse, memory_bank, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory_banks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_bank = await response.parse()
            assert_matches_type(MemoryBankListResponse, memory_bank, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        memory_bank = await async_client.memory_banks.register(
            memory_bank_id="memory_bank_id",
            params={
                "chunk_size_in_tokens": 0,
                "embedding_model": "embedding_model",
                "memory_bank_type": "vector",
            },
        )
        assert memory_bank is None

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory_bank = await async_client.memory_banks.register(
            memory_bank_id="memory_bank_id",
            params={
                "chunk_size_in_tokens": 0,
                "embedding_model": "embedding_model",
                "memory_bank_type": "vector",
                "overlap_size_in_tokens": 0,
            },
            provider_id="provider_id",
            provider_memory_bank_id="provider_memory_bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert memory_bank is None

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory_banks.with_raw_response.register(
            memory_bank_id="memory_bank_id",
            params={
                "chunk_size_in_tokens": 0,
                "embedding_model": "embedding_model",
                "memory_bank_type": "vector",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_bank = await response.parse()
        assert memory_bank is None

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory_banks.with_streaming_response.register(
            memory_bank_id="memory_bank_id",
            params={
                "chunk_size_in_tokens": 0,
                "embedding_model": "embedding_model",
                "memory_bank_type": "vector",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_bank = await response.parse()
            assert memory_bank is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        memory_bank = await async_client.memory_banks.unregister(
            memory_bank_id="memory_bank_id",
        )
        assert memory_bank is None

    @parametrize
    async def test_method_unregister_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory_bank = await async_client.memory_banks.unregister(
            memory_bank_id="memory_bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert memory_bank is None

    @parametrize
    async def test_raw_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory_banks.with_raw_response.unregister(
            memory_bank_id="memory_bank_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory_bank = await response.parse()
        assert memory_bank is None

    @parametrize
    async def test_streaming_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory_banks.with_streaming_response.unregister(
            memory_bank_id="memory_bank_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory_bank = await response.parse()
            assert memory_bank is None

        assert cast(Any, response.is_closed) is True

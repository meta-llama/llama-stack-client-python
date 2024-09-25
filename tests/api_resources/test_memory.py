# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    QueryDocuments,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMemory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        memory = client.memory.create(
            body={},
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        memory = client.memory.create(
            body={},
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.memory.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.memory.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        memory = client.memory.retrieve(
            bank_id="bank_id",
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        memory = client.memory.retrieve(
            bank_id="bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.memory.with_raw_response.retrieve(
            bank_id="bank_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.memory.with_streaming_response.retrieve(
            bank_id="bank_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: LlamaStackClient) -> None:
        memory = client.memory.update(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        )
        assert memory is None

    @parametrize
    def test_method_update_with_all_params(self, client: LlamaStackClient) -> None:
        memory = client.memory.update(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
            ],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert memory is None

    @parametrize
    def test_raw_response_update(self, client: LlamaStackClient) -> None:
        response = client.memory.with_raw_response.update(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @parametrize
    def test_streaming_response_update(self, client: LlamaStackClient) -> None:
        with client.memory.with_streaming_response.update(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        memory = client.memory.list()
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        memory = client.memory.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.memory.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.memory.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_drop(self, client: LlamaStackClient) -> None:
        memory = client.memory.drop(
            bank_id="bank_id",
        )
        assert_matches_type(str, memory, path=["response"])

    @parametrize
    def test_method_drop_with_all_params(self, client: LlamaStackClient) -> None:
        memory = client.memory.drop(
            bank_id="bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(str, memory, path=["response"])

    @parametrize
    def test_raw_response_drop(self, client: LlamaStackClient) -> None:
        response = client.memory.with_raw_response.drop(
            bank_id="bank_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(str, memory, path=["response"])

    @parametrize
    def test_streaming_response_drop(self, client: LlamaStackClient) -> None:
        with client.memory.with_streaming_response.drop(
            bank_id="bank_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(str, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_insert(self, client: LlamaStackClient) -> None:
        memory = client.memory.insert(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        )
        assert memory is None

    @parametrize
    def test_method_insert_with_all_params(self, client: LlamaStackClient) -> None:
        memory = client.memory.insert(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
            ],
            ttl_seconds=0,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert memory is None

    @parametrize
    def test_raw_response_insert(self, client: LlamaStackClient) -> None:
        response = client.memory.with_raw_response.insert(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert memory is None

    @parametrize
    def test_streaming_response_insert(self, client: LlamaStackClient) -> None:
        with client.memory.with_streaming_response.insert(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_query(self, client: LlamaStackClient) -> None:
        memory = client.memory.query(
            bank_id="bank_id",
            query="string",
        )
        assert_matches_type(QueryDocuments, memory, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: LlamaStackClient) -> None:
        memory = client.memory.query(
            bank_id="bank_id",
            query="string",
            params={"foo": True},
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(QueryDocuments, memory, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: LlamaStackClient) -> None:
        response = client.memory.with_raw_response.query(
            bank_id="bank_id",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = response.parse()
        assert_matches_type(QueryDocuments, memory, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: LlamaStackClient) -> None:
        with client.memory.with_streaming_response.query(
            bank_id="bank_id",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = response.parse()
            assert_matches_type(QueryDocuments, memory, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMemory:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.create(
            body={},
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.create(
            body={},
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory.with_raw_response.create(
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory.with_streaming_response.create(
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.retrieve(
            bank_id="bank_id",
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.retrieve(
            bank_id="bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory.with_raw_response.retrieve(
            bank_id="bank_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory.with_streaming_response.retrieve(
            bank_id="bank_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.update(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        )
        assert memory is None

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.update(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
            ],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert memory is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory.with_raw_response.update(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory.with_streaming_response.update(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.list()
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(object, memory, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(object, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_drop(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.drop(
            bank_id="bank_id",
        )
        assert_matches_type(str, memory, path=["response"])

    @parametrize
    async def test_method_drop_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.drop(
            bank_id="bank_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(str, memory, path=["response"])

    @parametrize
    async def test_raw_response_drop(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory.with_raw_response.drop(
            bank_id="bank_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(str, memory, path=["response"])

    @parametrize
    async def test_streaming_response_drop(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory.with_streaming_response.drop(
            bank_id="bank_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(str, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_insert(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.insert(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        )
        assert memory is None

    @parametrize
    async def test_method_insert_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.insert(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                    "mime_type": "mime_type",
                },
            ],
            ttl_seconds=0,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert memory is None

    @parametrize
    async def test_raw_response_insert(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory.with_raw_response.insert(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert memory is None

    @parametrize
    async def test_streaming_response_insert(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory.with_streaming_response.insert(
            bank_id="bank_id",
            documents=[
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
                {
                    "content": "string",
                    "document_id": "document_id",
                    "metadata": {"foo": True},
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert memory is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_query(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.query(
            bank_id="bank_id",
            query="string",
        )
        assert_matches_type(QueryDocuments, memory, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        memory = await async_client.memory.query(
            bank_id="bank_id",
            query="string",
            params={"foo": True},
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(QueryDocuments, memory, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.memory.with_raw_response.query(
            bank_id="bank_id",
            query="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        memory = await response.parse()
        assert_matches_type(QueryDocuments, memory, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.memory.with_streaming_response.query(
            bank_id="bank_id",
            query="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            memory = await response.parse()
            assert_matches_type(QueryDocuments, memory, path=["response"])

        assert cast(Any, response.is_closed) is True

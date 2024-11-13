# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import Shield

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        shield = client.shields.retrieve(
            identifier="identifier",
        )
        assert_matches_type(Optional[Shield], shield, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        shield = client.shields.retrieve(
            identifier="identifier",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[Shield], shield, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.retrieve(
            identifier="identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(Optional[Shield], shield, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.shields.with_streaming_response.retrieve(
            identifier="identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = response.parse()
            assert_matches_type(Optional[Shield], shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        shield = client.shields.list()
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        shield = client.shields.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.shields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = response.parse()
            assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        shield = client.shields.register(
            shield_id="shield_id",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        shield = client.shields.register(
            shield_id="shield_id",
            params={"foo": True},
            provider_id="provider_id",
            provider_shield_id="provider_shield_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.register(
            shield_id="shield_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with client.shields.with_streaming_response.register(
            shield_id="shield_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = response.parse()
            assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.retrieve(
            identifier="identifier",
        )
        assert_matches_type(Optional[Shield], shield, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.retrieve(
            identifier="identifier",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[Shield], shield, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.retrieve(
            identifier="identifier",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(Optional[Shield], shield, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.shields.with_streaming_response.retrieve(
            identifier="identifier",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = await response.parse()
            assert_matches_type(Optional[Shield], shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.list()
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.shields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = await response.parse()
            assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.register(
            shield_id="shield_id",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.register(
            shield_id="shield_id",
            params={"foo": True},
            provider_id="provider_id",
            provider_shield_id="provider_shield_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.register(
            shield_id="shield_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(Shield, shield, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.shields.with_streaming_response.register(
            shield_id="shield_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = await response.parse()
            assert_matches_type(Shield, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

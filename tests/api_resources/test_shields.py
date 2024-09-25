# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import ShieldSpec

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        shield = client.shields.list()
        assert_matches_type(ShieldSpec, shield, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        shield = client.shields.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ShieldSpec, shield, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(ShieldSpec, shield, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.shields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = response.parse()
            assert_matches_type(ShieldSpec, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: LlamaStackClient) -> None:
        shield = client.shields.get(
            shield_type="shield_type",
        )
        assert_matches_type(Optional[ShieldSpec], shield, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: LlamaStackClient) -> None:
        shield = client.shields.get(
            shield_type="shield_type",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[ShieldSpec], shield, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LlamaStackClient) -> None:
        response = client.shields.with_raw_response.get(
            shield_type="shield_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = response.parse()
        assert_matches_type(Optional[ShieldSpec], shield, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LlamaStackClient) -> None:
        with client.shields.with_streaming_response.get(
            shield_type="shield_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = response.parse()
            assert_matches_type(Optional[ShieldSpec], shield, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncShields:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.list()
        assert_matches_type(ShieldSpec, shield, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ShieldSpec, shield, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(ShieldSpec, shield, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.shields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = await response.parse()
            assert_matches_type(ShieldSpec, shield, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.get(
            shield_type="shield_type",
        )
        assert_matches_type(Optional[ShieldSpec], shield, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        shield = await async_client.shields.get(
            shield_type="shield_type",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[ShieldSpec], shield, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.shields.with_raw_response.get(
            shield_type="shield_type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        shield = await response.parse()
        assert_matches_type(Optional[ShieldSpec], shield, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.shields.with_streaming_response.get(
            shield_type="shield_type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            shield = await response.parse()
            assert_matches_type(Optional[ShieldSpec], shield, path=["response"])

        assert cast(Any, response.is_closed) is True

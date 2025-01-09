# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import Tool

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTools:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        tool = client.tools.list()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        tool = client.tools.list(
            tool_group_id="tool_group_id",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: LlamaStackClient) -> None:
        tool = client.tools.get(
            tool_name="tool_name",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: LlamaStackClient) -> None:
        tool = client.tools.get(
            tool_name="tool_name",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LlamaStackClient) -> None:
        response = client.tools.with_raw_response.get(
            tool_name="tool_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LlamaStackClient) -> None:
        with client.tools.with_streaming_response.get(
            tool_name="tool_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTools:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        tool = await async_client.tools.list()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        tool = await async_client.tools.list(
            tool_group_id="tool_group_id",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tools.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tools.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaStackClient) -> None:
        tool = await async_client.tools.get(
            tool_name="tool_name",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        tool = await async_client.tools.get(
            tool_name="tool_name",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tools.with_raw_response.get(
            tool_name="tool_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(Tool, tool, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tools.with_streaming_response.get(
            tool_name="tool_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(Tool, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

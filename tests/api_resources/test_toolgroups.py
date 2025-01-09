# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    ToolGroup,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolgroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        toolgroup = client.toolgroups.list()
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        toolgroup = client.toolgroups.list(
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.toolgroups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = response.parse()
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.toolgroups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolgroup = response.parse()
            assert_matches_type(ToolGroup, toolgroup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: LlamaStackClient) -> None:
        toolgroup = client.toolgroups.get(
            toolgroup_id="toolgroup_id",
        )
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: LlamaStackClient) -> None:
        toolgroup = client.toolgroups.get(
            toolgroup_id="toolgroup_id",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LlamaStackClient) -> None:
        response = client.toolgroups.with_raw_response.get(
            toolgroup_id="toolgroup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = response.parse()
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LlamaStackClient) -> None:
        with client.toolgroups.with_streaming_response.get(
            toolgroup_id="toolgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolgroup = response.parse()
            assert_matches_type(ToolGroup, toolgroup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        toolgroup = client.toolgroups.register(
            provider_id="provider_id",
            toolgroup_id="toolgroup_id",
        )
        assert toolgroup is None

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        toolgroup = client.toolgroups.register(
            provider_id="provider_id",
            toolgroup_id="toolgroup_id",
            args={"foo": True},
            mcp_config={
                "command": "command",
                "type": "inline",
                "args": ["string"],
                "env": {"foo": True},
            },
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert toolgroup is None

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        response = client.toolgroups.with_raw_response.register(
            provider_id="provider_id",
            toolgroup_id="toolgroup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = response.parse()
        assert toolgroup is None

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with client.toolgroups.with_streaming_response.register(
            provider_id="provider_id",
            toolgroup_id="toolgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolgroup = response.parse()
            assert toolgroup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unregister(self, client: LlamaStackClient) -> None:
        toolgroup = client.toolgroups.unregister(
            tool_group_id="tool_group_id",
        )
        assert toolgroup is None

    @parametrize
    def test_method_unregister_with_all_params(self, client: LlamaStackClient) -> None:
        toolgroup = client.toolgroups.unregister(
            tool_group_id="tool_group_id",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert toolgroup is None

    @parametrize
    def test_raw_response_unregister(self, client: LlamaStackClient) -> None:
        response = client.toolgroups.with_raw_response.unregister(
            tool_group_id="tool_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = response.parse()
        assert toolgroup is None

    @parametrize
    def test_streaming_response_unregister(self, client: LlamaStackClient) -> None:
        with client.toolgroups.with_streaming_response.unregister(
            tool_group_id="tool_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolgroup = response.parse()
            assert toolgroup is None

        assert cast(Any, response.is_closed) is True


class TestAsyncToolgroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        toolgroup = await async_client.toolgroups.list()
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        toolgroup = await async_client.toolgroups.list(
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.toolgroups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = await response.parse()
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.toolgroups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolgroup = await response.parse()
            assert_matches_type(ToolGroup, toolgroup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaStackClient) -> None:
        toolgroup = await async_client.toolgroups.get(
            toolgroup_id="toolgroup_id",
        )
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        toolgroup = await async_client.toolgroups.get(
            toolgroup_id="toolgroup_id",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.toolgroups.with_raw_response.get(
            toolgroup_id="toolgroup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = await response.parse()
        assert_matches_type(ToolGroup, toolgroup, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.toolgroups.with_streaming_response.get(
            toolgroup_id="toolgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolgroup = await response.parse()
            assert_matches_type(ToolGroup, toolgroup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        toolgroup = await async_client.toolgroups.register(
            provider_id="provider_id",
            toolgroup_id="toolgroup_id",
        )
        assert toolgroup is None

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        toolgroup = await async_client.toolgroups.register(
            provider_id="provider_id",
            toolgroup_id="toolgroup_id",
            args={"foo": True},
            mcp_config={
                "command": "command",
                "type": "inline",
                "args": ["string"],
                "env": {"foo": True},
            },
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert toolgroup is None

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.toolgroups.with_raw_response.register(
            provider_id="provider_id",
            toolgroup_id="toolgroup_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = await response.parse()
        assert toolgroup is None

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.toolgroups.with_streaming_response.register(
            provider_id="provider_id",
            toolgroup_id="toolgroup_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolgroup = await response.parse()
            assert toolgroup is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        toolgroup = await async_client.toolgroups.unregister(
            tool_group_id="tool_group_id",
        )
        assert toolgroup is None

    @parametrize
    async def test_method_unregister_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        toolgroup = await async_client.toolgroups.unregister(
            tool_group_id="tool_group_id",
            x_llama_stack_client_version="X-LlamaStack-Client-Version",
            x_llama_stack_provider_data="X-LlamaStack-Provider-Data",
        )
        assert toolgroup is None

    @parametrize
    async def test_raw_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.toolgroups.with_raw_response.unregister(
            tool_group_id="tool_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        toolgroup = await response.parse()
        assert toolgroup is None

    @parametrize
    async def test_streaming_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.toolgroups.with_streaming_response.unregister(
            tool_group_id="tool_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            toolgroup = await response.parse()
            assert toolgroup is None

        assert cast(Any, response.is_closed) is True

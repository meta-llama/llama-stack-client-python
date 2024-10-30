# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.agents import Turn, AgentsTurnStreamChunk

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTurns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create_overload_1(self, client: LlamaStackClient) -> None:
        turn = client.agents.turns.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
        )
        assert_matches_type(AgentsTurnStreamChunk, turn, path=["response"])

    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: LlamaStackClient) -> None:
        turn = client.agents.turns.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
            ],
            session_id="session_id",
            attachments=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
            ],
            stream=False,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(AgentsTurnStreamChunk, turn, path=["response"])

    @parametrize
    def test_raw_response_create_overload_1(self, client: LlamaStackClient) -> None:
        response = client.agents.turns.with_raw_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = response.parse()
        assert_matches_type(AgentsTurnStreamChunk, turn, path=["response"])

    @parametrize
    def test_streaming_response_create_overload_1(self, client: LlamaStackClient) -> None:
        with client.agents.turns.with_streaming_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = response.parse()
            assert_matches_type(AgentsTurnStreamChunk, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_create_overload_2(self, client: LlamaStackClient) -> None:
        turn_stream = client.agents.turns.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
            stream=True,
        )
        turn_stream.response.close()

    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: LlamaStackClient) -> None:
        turn_stream = client.agents.turns.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
            ],
            session_id="session_id",
            stream=True,
            attachments=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
            ],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        turn_stream.response.close()

    @parametrize
    def test_raw_response_create_overload_2(self, client: LlamaStackClient) -> None:
        response = client.agents.turns.with_raw_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @parametrize
    def test_streaming_response_create_overload_2(self, client: LlamaStackClient) -> None:
        with client.agents.turns.with_streaming_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        turn = client.agents.turns.retrieve(
            agent_id="agent_id",
            turn_id="turn_id",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        turn = client.agents.turns.retrieve(
            agent_id="agent_id",
            turn_id="turn_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.agents.turns.with_raw_response.retrieve(
            agent_id="agent_id",
            turn_id="turn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.agents.turns.with_streaming_response.retrieve(
            agent_id="agent_id",
            turn_id="turn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTurns:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.turns.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
        )
        assert_matches_type(AgentsTurnStreamChunk, turn, path=["response"])

    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.turns.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
            ],
            session_id="session_id",
            attachments=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
            ],
            stream=False,
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(AgentsTurnStreamChunk, turn, path=["response"])

    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.turns.with_raw_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = await response.parse()
        assert_matches_type(AgentsTurnStreamChunk, turn, path=["response"])

    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.turns.with_streaming_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = await response.parse()
            assert_matches_type(AgentsTurnStreamChunk, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        turn_stream = await async_client.agents.turns.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
            stream=True,
        )
        await turn_stream.response.aclose()

    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        turn_stream = await async_client.agents.turns.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
                {
                    "content": "string",
                    "role": "user",
                    "context": "string",
                },
            ],
            session_id="session_id",
            stream=True,
            attachments=[
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
                {
                    "content": "string",
                    "mime_type": "mime_type",
                },
            ],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        await turn_stream.response.aclose()

    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.turns.with_raw_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
            stream=True,
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.turns.with_streaming_response.create(
            agent_id="agent_id",
            messages=[
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
                {
                    "content": "string",
                    "role": "user",
                },
            ],
            session_id="session_id",
            stream=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.turns.retrieve(
            agent_id="agent_id",
            turn_id="turn_id",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        turn = await async_client.agents.turns.retrieve(
            agent_id="agent_id",
            turn_id="turn_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.turns.with_raw_response.retrieve(
            agent_id="agent_id",
            turn_id="turn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        turn = await response.parse()
        assert_matches_type(Turn, turn, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.turns.with_streaming_response.retrieve(
            agent_id="agent_id",
            turn_id="turn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            turn = await response.parse()
            assert_matches_type(Turn, turn, path=["response"])

        assert cast(Any, response.is_closed) is True

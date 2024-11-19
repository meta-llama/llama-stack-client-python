# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.agents import (
    Session,
    SessionCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        session = client.agents.session.create(
            agent_id="agent_id",
            session_name="session_name",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        session = client.agents.session.create(
            agent_id="agent_id",
            session_name="session_name",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.agents.session.with_raw_response.create(
            agent_id="agent_id",
            session_name="session_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.agents.session.with_streaming_response.create(
            agent_id="agent_id",
            session_name="session_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        session = client.agents.session.retrieve(
            agent_id="agent_id",
            session_id="session_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        session = client.agents.session.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            turn_ids=["string"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.agents.session.with_raw_response.retrieve(
            agent_id="agent_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.agents.session.with_streaming_response.retrieve(
            agent_id="agent_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LlamaStackClient) -> None:
        session = client.agents.session.delete(
            agent_id="agent_id",
            session_id="session_id",
        )
        assert session is None

    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaStackClient) -> None:
        session = client.agents.session.delete(
            agent_id="agent_id",
            session_id="session_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert session is None

    @parametrize
    def test_raw_response_delete(self, client: LlamaStackClient) -> None:
        response = client.agents.session.with_raw_response.delete(
            agent_id="agent_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @parametrize
    def test_streaming_response_delete(self, client: LlamaStackClient) -> None:
        with client.agents.session.with_streaming_response.delete(
            agent_id="agent_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSession:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        session = await async_client.agents.session.create(
            agent_id="agent_id",
            session_name="session_name",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        session = await async_client.agents.session.create(
            agent_id="agent_id",
            session_name="session_name",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.session.with_raw_response.create(
            agent_id="agent_id",
            session_name="session_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionCreateResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.session.with_streaming_response.create(
            agent_id="agent_id",
            session_name="session_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionCreateResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        session = await async_client.agents.session.retrieve(
            agent_id="agent_id",
            session_id="session_id",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        session = await async_client.agents.session.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            turn_ids=["string"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.session.with_raw_response.retrieve(
            agent_id="agent_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.session.with_streaming_response.retrieve(
            agent_id="agent_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaStackClient) -> None:
        session = await async_client.agents.session.delete(
            agent_id="agent_id",
            session_id="session_id",
        )
        assert session is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        session = await async_client.agents.session.delete(
            agent_id="agent_id",
            session_id="session_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert session is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.session.with_raw_response.delete(
            agent_id="agent_id",
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.session.with_streaming_response.delete(
            agent_id="agent_id",
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.agents import StepRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSteps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        step = client.agents.steps.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            step_id="step_id",
            turn_id="turn_id",
        )
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        step = client.agents.steps.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            step_id="step_id",
            turn_id="turn_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.agents.steps.with_raw_response.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            step_id="step_id",
            turn_id="turn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = response.parse()
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.agents.steps.with_streaming_response.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            step_id="step_id",
            turn_id="turn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = response.parse()
            assert_matches_type(StepRetrieveResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSteps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        step = await async_client.agents.steps.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            step_id="step_id",
            turn_id="turn_id",
        )
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        step = await async_client.agents.steps.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            step_id="step_id",
            turn_id="turn_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.steps.with_raw_response.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            step_id="step_id",
            turn_id="turn_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        step = await response.parse()
        assert_matches_type(StepRetrieveResponse, step, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.steps.with_streaming_response.retrieve(
            agent_id="agent_id",
            session_id="session_id",
            step_id="step_id",
            turn_id="turn_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            step = await response.parse()
            assert_matches_type(StepRetrieveResponse, step, path=["response"])

        assert cast(Any, response.is_closed) is True

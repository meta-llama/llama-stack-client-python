# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import AgentCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        agent = client.agents.create(
            agent_config={
                "instructions": "instructions",
                "model": "model",
            },
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        agent = client.agents.create(
            agent_config={
                "instructions": "instructions",
                "model": "model",
                "client_tools": [
                    {
                        "name": "name",
                        "description": "description",
                        "metadata": {"foo": True},
                        "parameters": [
                            {
                                "description": "description",
                                "name": "name",
                                "parameter_type": "parameter_type",
                                "required": True,
                                "default": True,
                            }
                        ],
                    }
                ],
                "enable_session_persistence": True,
                "input_shields": ["string"],
                "max_infer_iters": 0,
                "output_shields": ["string"],
                "response_format": {
                    "json_schema": {"foo": True},
                    "type": "json_schema",
                },
                "sampling_params": {
                    "strategy": {"type": "greedy"},
                    "max_tokens": 0,
                    "repetition_penalty": 0,
                },
                "tool_choice": "auto",
                "tool_config": {
                    "system_message_behavior": "append",
                    "tool_choice": "auto",
                    "tool_prompt_format": "json",
                },
                "tool_prompt_format": "json",
                "toolgroups": ["string"],
            },
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.agents.with_raw_response.create(
            agent_config={
                "instructions": "instructions",
                "model": "model",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.agents.with_streaming_response.create(
            agent_config={
                "instructions": "instructions",
                "model": "model",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: LlamaStackClient) -> None:
        agent = client.agents.delete(
            "agent_id",
        )
        assert agent is None

    @parametrize
    def test_raw_response_delete(self, client: LlamaStackClient) -> None:
        response = client.agents.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert agent is None

    @parametrize
    def test_streaming_response_delete(self, client: LlamaStackClient) -> None:
        with client.agents.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: LlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.agents.with_raw_response.delete(
                "",
            )


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        agent = await async_client.agents.create(
            agent_config={
                "instructions": "instructions",
                "model": "model",
            },
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        agent = await async_client.agents.create(
            agent_config={
                "instructions": "instructions",
                "model": "model",
                "client_tools": [
                    {
                        "name": "name",
                        "description": "description",
                        "metadata": {"foo": True},
                        "parameters": [
                            {
                                "description": "description",
                                "name": "name",
                                "parameter_type": "parameter_type",
                                "required": True,
                                "default": True,
                            }
                        ],
                    }
                ],
                "enable_session_persistence": True,
                "input_shields": ["string"],
                "max_infer_iters": 0,
                "output_shields": ["string"],
                "response_format": {
                    "json_schema": {"foo": True},
                    "type": "json_schema",
                },
                "sampling_params": {
                    "strategy": {"type": "greedy"},
                    "max_tokens": 0,
                    "repetition_penalty": 0,
                },
                "tool_choice": "auto",
                "tool_config": {
                    "system_message_behavior": "append",
                    "tool_choice": "auto",
                    "tool_prompt_format": "json",
                },
                "tool_prompt_format": "json",
                "toolgroups": ["string"],
            },
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.with_raw_response.create(
            agent_config={
                "instructions": "instructions",
                "model": "model",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.with_streaming_response.create(
            agent_config={
                "instructions": "instructions",
                "model": "model",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaStackClient) -> None:
        agent = await async_client.agents.delete(
            "agent_id",
        )
        assert agent is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.agents.with_raw_response.delete(
            "agent_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert agent is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.agents.with_streaming_response.delete(
            "agent_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert agent is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaStackClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.agents.with_raw_response.delete(
                "",
            )

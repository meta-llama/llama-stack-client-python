# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import (
    ScoringFnDefWithProvider,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScoringFunctions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.retrieve(
            name="name",
        )
        assert_matches_type(Optional[ScoringFnDefWithProvider], scoring_function, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.retrieve(
            name="name",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[ScoringFnDefWithProvider], scoring_function, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: LlamaStackClient) -> None:
        response = client.scoring_functions.with_raw_response.retrieve(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = response.parse()
        assert_matches_type(Optional[ScoringFnDefWithProvider], scoring_function, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaStackClient) -> None:
        with client.scoring_functions.with_streaming_response.retrieve(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = response.parse()
            assert_matches_type(Optional[ScoringFnDefWithProvider], scoring_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.list()
        assert_matches_type(ScoringFnDefWithProvider, scoring_function, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ScoringFnDefWithProvider, scoring_function, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.scoring_functions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = response.parse()
        assert_matches_type(ScoringFnDefWithProvider, scoring_function, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.scoring_functions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = response.parse()
            assert_matches_type(ScoringFnDefWithProvider, scoring_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.register(
            function_def={
                "identifier": "identifier",
                "metadata": {"foo": True},
                "parameters": [
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                ],
                "provider_id": "provider_id",
                "return_type": {"type": "string"},
            },
        )
        assert scoring_function is None

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        scoring_function = client.scoring_functions.register(
            function_def={
                "identifier": "identifier",
                "metadata": {"foo": True},
                "parameters": [
                    {
                        "name": "name",
                        "type": {"type": "string"},
                        "description": "description",
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                        "description": "description",
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                        "description": "description",
                    },
                ],
                "provider_id": "provider_id",
                "return_type": {"type": "string"},
                "context": {
                    "judge_model": "judge_model",
                    "judge_score_regex": ["string", "string", "string"],
                    "prompt_template": "prompt_template",
                },
                "description": "description",
            },
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert scoring_function is None

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        response = client.scoring_functions.with_raw_response.register(
            function_def={
                "identifier": "identifier",
                "metadata": {"foo": True},
                "parameters": [
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                ],
                "provider_id": "provider_id",
                "return_type": {"type": "string"},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = response.parse()
        assert scoring_function is None

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with client.scoring_functions.with_streaming_response.register(
            function_def={
                "identifier": "identifier",
                "metadata": {"foo": True},
                "parameters": [
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                ],
                "provider_id": "provider_id",
                "return_type": {"type": "string"},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = response.parse()
            assert scoring_function is None

        assert cast(Any, response.is_closed) is True


class TestAsyncScoringFunctions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.retrieve(
            name="name",
        )
        assert_matches_type(Optional[ScoringFnDefWithProvider], scoring_function, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.retrieve(
            name="name",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(Optional[ScoringFnDefWithProvider], scoring_function, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.scoring_functions.with_raw_response.retrieve(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = await response.parse()
        assert_matches_type(Optional[ScoringFnDefWithProvider], scoring_function, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.scoring_functions.with_streaming_response.retrieve(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = await response.parse()
            assert_matches_type(Optional[ScoringFnDefWithProvider], scoring_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.list()
        assert_matches_type(ScoringFnDefWithProvider, scoring_function, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ScoringFnDefWithProvider, scoring_function, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.scoring_functions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = await response.parse()
        assert_matches_type(ScoringFnDefWithProvider, scoring_function, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.scoring_functions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = await response.parse()
            assert_matches_type(ScoringFnDefWithProvider, scoring_function, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.register(
            function_def={
                "identifier": "identifier",
                "metadata": {"foo": True},
                "parameters": [
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                ],
                "provider_id": "provider_id",
                "return_type": {"type": "string"},
            },
        )
        assert scoring_function is None

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        scoring_function = await async_client.scoring_functions.register(
            function_def={
                "identifier": "identifier",
                "metadata": {"foo": True},
                "parameters": [
                    {
                        "name": "name",
                        "type": {"type": "string"},
                        "description": "description",
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                        "description": "description",
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                        "description": "description",
                    },
                ],
                "provider_id": "provider_id",
                "return_type": {"type": "string"},
                "context": {
                    "judge_model": "judge_model",
                    "judge_score_regex": ["string", "string", "string"],
                    "prompt_template": "prompt_template",
                },
                "description": "description",
            },
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert scoring_function is None

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.scoring_functions.with_raw_response.register(
            function_def={
                "identifier": "identifier",
                "metadata": {"foo": True},
                "parameters": [
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                ],
                "provider_id": "provider_id",
                "return_type": {"type": "string"},
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        scoring_function = await response.parse()
        assert scoring_function is None

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.scoring_functions.with_streaming_response.register(
            function_def={
                "identifier": "identifier",
                "metadata": {"foo": True},
                "parameters": [
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                    {
                        "name": "name",
                        "type": {"type": "string"},
                    },
                ],
                "provider_id": "provider_id",
                "return_type": {"type": "string"},
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            scoring_function = await response.parse()
            assert scoring_function is None

        assert cast(Any, response.is_closed) is True

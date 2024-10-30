# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import RewardScoringResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRewardScoring:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_score(self, client: LlamaStackClient) -> None:
        reward_scoring = client.reward_scoring.score(
            dialog_generations=[
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
            ],
            model="model",
        )
        assert_matches_type(RewardScoringResponse, reward_scoring, path=["response"])

    @parametrize
    def test_method_score_with_all_params(self, client: LlamaStackClient) -> None:
        reward_scoring = client.reward_scoring.score(
            dialog_generations=[
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
            ],
            model="model",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(RewardScoringResponse, reward_scoring, path=["response"])

    @parametrize
    def test_raw_response_score(self, client: LlamaStackClient) -> None:
        response = client.reward_scoring.with_raw_response.score(
            dialog_generations=[
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward_scoring = response.parse()
        assert_matches_type(RewardScoringResponse, reward_scoring, path=["response"])

    @parametrize
    def test_streaming_response_score(self, client: LlamaStackClient) -> None:
        with client.reward_scoring.with_streaming_response.score(
            dialog_generations=[
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward_scoring = response.parse()
            assert_matches_type(RewardScoringResponse, reward_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRewardScoring:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_score(self, async_client: AsyncLlamaStackClient) -> None:
        reward_scoring = await async_client.reward_scoring.score(
            dialog_generations=[
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
            ],
            model="model",
        )
        assert_matches_type(RewardScoringResponse, reward_scoring, path=["response"])

    @parametrize
    async def test_method_score_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        reward_scoring = await async_client.reward_scoring.score(
            dialog_generations=[
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
            ],
            model="model",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(RewardScoringResponse, reward_scoring, path=["response"])

    @parametrize
    async def test_raw_response_score(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.reward_scoring.with_raw_response.score(
            dialog_generations=[
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
            ],
            model="model",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        reward_scoring = await response.parse()
        assert_matches_type(RewardScoringResponse, reward_scoring, path=["response"])

    @parametrize
    async def test_streaming_response_score(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.reward_scoring.with_streaming_response.score(
            dialog_generations=[
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
                {
                    "dialog": [
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
                    "sampled_generations": [
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
                },
            ],
            model="model",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            reward_scoring = await response.parse()
            assert_matches_type(RewardScoringResponse, reward_scoring, path=["response"])

        assert cast(Any, response.is_closed) is True

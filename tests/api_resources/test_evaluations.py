# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import EvaluationJob

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_text_generation(self, client: LlamaStackClient) -> None:
        evaluation = client.evaluations.text_generation(
            metrics=["perplexity", "rouge", "bleu"],
        )
        assert_matches_type(EvaluationJob, evaluation, path=["response"])

    @parametrize
    def test_method_text_generation_with_all_params(self, client: LlamaStackClient) -> None:
        evaluation = client.evaluations.text_generation(
            metrics=["perplexity", "rouge", "bleu"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(EvaluationJob, evaluation, path=["response"])

    @parametrize
    def test_raw_response_text_generation(self, client: LlamaStackClient) -> None:
        response = client.evaluations.with_raw_response.text_generation(
            metrics=["perplexity", "rouge", "bleu"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluationJob, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_text_generation(self, client: LlamaStackClient) -> None:
        with client.evaluations.with_streaming_response.text_generation(
            metrics=["perplexity", "rouge", "bleu"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluationJob, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_text_generation(self, async_client: AsyncLlamaStackClient) -> None:
        evaluation = await async_client.evaluations.text_generation(
            metrics=["perplexity", "rouge", "bleu"],
        )
        assert_matches_type(EvaluationJob, evaluation, path=["response"])

    @parametrize
    async def test_method_text_generation_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        evaluation = await async_client.evaluations.text_generation(
            metrics=["perplexity", "rouge", "bleu"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(EvaluationJob, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_text_generation(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.evaluations.with_raw_response.text_generation(
            metrics=["perplexity", "rouge", "bleu"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluationJob, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_text_generation(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.evaluations.with_streaming_response.text_generation(
            metrics=["perplexity", "rouge", "bleu"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluationJob, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import EvaluationJob

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuestionAnswering:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: LlamaStackClient) -> None:
        question_answering = client.evaluate.question_answering.create(
            metrics=["em", "f1"],
        )
        assert_matches_type(EvaluationJob, question_answering, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: LlamaStackClient) -> None:
        question_answering = client.evaluate.question_answering.create(
            metrics=["em", "f1"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(EvaluationJob, question_answering, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: LlamaStackClient) -> None:
        response = client.evaluate.question_answering.with_raw_response.create(
            metrics=["em", "f1"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question_answering = response.parse()
        assert_matches_type(EvaluationJob, question_answering, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: LlamaStackClient) -> None:
        with client.evaluate.question_answering.with_streaming_response.create(
            metrics=["em", "f1"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question_answering = response.parse()
            assert_matches_type(EvaluationJob, question_answering, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncQuestionAnswering:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaStackClient) -> None:
        question_answering = await async_client.evaluate.question_answering.create(
            metrics=["em", "f1"],
        )
        assert_matches_type(EvaluationJob, question_answering, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        question_answering = await async_client.evaluate.question_answering.create(
            metrics=["em", "f1"],
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(EvaluationJob, question_answering, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.evaluate.question_answering.with_raw_response.create(
            metrics=["em", "f1"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question_answering = await response.parse()
        assert_matches_type(EvaluationJob, question_answering, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.evaluate.question_answering.with_streaming_response.create(
            metrics=["em", "f1"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question_answering = await response.parse()
            assert_matches_type(EvaluationJob, question_answering, path=["response"])

        assert cast(Any, response.is_closed) is True

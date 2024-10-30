# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types import PaginatedRowsResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasetio:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_rows_paginated(self, client: LlamaStackClient) -> None:
        datasetio = client.datasetio.get_rows_paginated(
            dataset_id="dataset_id",
            rows_in_page=0,
        )
        assert_matches_type(PaginatedRowsResult, datasetio, path=["response"])

    @parametrize
    def test_method_get_rows_paginated_with_all_params(self, client: LlamaStackClient) -> None:
        datasetio = client.datasetio.get_rows_paginated(
            dataset_id="dataset_id",
            rows_in_page=0,
            filter_condition="filter_condition",
            page_token="page_token",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(PaginatedRowsResult, datasetio, path=["response"])

    @parametrize
    def test_raw_response_get_rows_paginated(self, client: LlamaStackClient) -> None:
        response = client.datasetio.with_raw_response.get_rows_paginated(
            dataset_id="dataset_id",
            rows_in_page=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasetio = response.parse()
        assert_matches_type(PaginatedRowsResult, datasetio, path=["response"])

    @parametrize
    def test_streaming_response_get_rows_paginated(self, client: LlamaStackClient) -> None:
        with client.datasetio.with_streaming_response.get_rows_paginated(
            dataset_id="dataset_id",
            rows_in_page=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasetio = response.parse()
            assert_matches_type(PaginatedRowsResult, datasetio, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasetio:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get_rows_paginated(self, async_client: AsyncLlamaStackClient) -> None:
        datasetio = await async_client.datasetio.get_rows_paginated(
            dataset_id="dataset_id",
            rows_in_page=0,
        )
        assert_matches_type(PaginatedRowsResult, datasetio, path=["response"])

    @parametrize
    async def test_method_get_rows_paginated_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        datasetio = await async_client.datasetio.get_rows_paginated(
            dataset_id="dataset_id",
            rows_in_page=0,
            filter_condition="filter_condition",
            page_token="page_token",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(PaginatedRowsResult, datasetio, path=["response"])

    @parametrize
    async def test_raw_response_get_rows_paginated(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.datasetio.with_raw_response.get_rows_paginated(
            dataset_id="dataset_id",
            rows_in_page=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        datasetio = await response.parse()
        assert_matches_type(PaginatedRowsResult, datasetio, path=["response"])

    @parametrize
    async def test_streaming_response_get_rows_paginated(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.datasetio.with_streaming_response.get_rows_paginated(
            dataset_id="dataset_id",
            rows_in_page=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            datasetio = await response.parse()
            assert_matches_type(PaginatedRowsResult, datasetio, path=["response"])

        assert cast(Any, response.is_closed) is True

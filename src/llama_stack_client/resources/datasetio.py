# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import datasetio_get_rows_paginated_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.paginated_rows_result import PaginatedRowsResult

__all__ = ["DatasetioResource", "AsyncDatasetioResource"]


class DatasetioResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DatasetioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return DatasetioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return DatasetioResourceWithStreamingResponse(self)

    def get_rows_paginated(
        self,
        *,
        dataset_id: str,
        rows_in_page: int,
        filter_condition: str | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedRowsResult:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._get(
            "/datasetio/get_rows_paginated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "dataset_id": dataset_id,
                        "rows_in_page": rows_in_page,
                        "filter_condition": filter_condition,
                        "page_token": page_token,
                    },
                    datasetio_get_rows_paginated_params.DatasetioGetRowsPaginatedParams,
                ),
            ),
            cast_to=PaginatedRowsResult,
        )


class AsyncDatasetioResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDatasetioResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetioResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetioResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncDatasetioResourceWithStreamingResponse(self)

    async def get_rows_paginated(
        self,
        *,
        dataset_id: str,
        rows_in_page: int,
        filter_condition: str | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaginatedRowsResult:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/datasetio/get_rows_paginated",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "dataset_id": dataset_id,
                        "rows_in_page": rows_in_page,
                        "filter_condition": filter_condition,
                        "page_token": page_token,
                    },
                    datasetio_get_rows_paginated_params.DatasetioGetRowsPaginatedParams,
                ),
            ),
            cast_to=PaginatedRowsResult,
        )


class DatasetioResourceWithRawResponse:
    def __init__(self, datasetio: DatasetioResource) -> None:
        self._datasetio = datasetio

        self.get_rows_paginated = to_raw_response_wrapper(
            datasetio.get_rows_paginated,
        )


class AsyncDatasetioResourceWithRawResponse:
    def __init__(self, datasetio: AsyncDatasetioResource) -> None:
        self._datasetio = datasetio

        self.get_rows_paginated = async_to_raw_response_wrapper(
            datasetio.get_rows_paginated,
        )


class DatasetioResourceWithStreamingResponse:
    def __init__(self, datasetio: DatasetioResource) -> None:
        self._datasetio = datasetio

        self.get_rows_paginated = to_streamed_response_wrapper(
            datasetio.get_rows_paginated,
        )


class AsyncDatasetioResourceWithStreamingResponse:
    def __init__(self, datasetio: AsyncDatasetioResource) -> None:
        self._datasetio = datasetio

        self.get_rows_paginated = async_to_streamed_response_wrapper(
            datasetio.get_rows_paginated,
        )

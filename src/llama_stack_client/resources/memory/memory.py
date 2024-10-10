# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional

import httpx

from ...types import (
    memory_drop_params,
    memory_query_params,
    memory_create_params,
    memory_insert_params,
    memory_update_params,
    memory_retrieve_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from .documents import (
    DocumentsResource,
    AsyncDocumentsResource,
    DocumentsResourceWithRawResponse,
    AsyncDocumentsResourceWithRawResponse,
    DocumentsResourceWithStreamingResponse,
    AsyncDocumentsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.query_documents import QueryDocuments
from ...types.memory_list_response import MemoryListResponse
from ...types.memory_create_response import MemoryCreateResponse
from ...types.memory_retrieve_response import MemoryRetrieveResponse

__all__ = ["MemoryResource", "AsyncMemoryResource"]


class MemoryResource(SyncAPIResource):
    @cached_property
    def documents(self) -> DocumentsResource:
        return DocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return MemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return MemoryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: memory_create_params.Config,
        name: str,
        url: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryCreateResponse:
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
        return self._post(
            "/memory/create",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "url": url,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryCreateResponse,
        )

    def retrieve(
        self,
        *,
        bank_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemoryRetrieveResponse]:
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
            "/memory/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"bank_id": bank_id}, memory_retrieve_params.MemoryRetrieveParams),
            ),
            cast_to=MemoryRetrieveResponse,
        )

    def update(
        self,
        *,
        bank_id: str,
        documents: Iterable[memory_update_params.Document],
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._post(
            "/memory/update",
            body=maybe_transform(
                {
                    "bank_id": bank_id,
                    "documents": documents,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        *,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._get(
            "/memory/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryListResponse,
        )

    def drop(
        self,
        *,
        bank_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
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
        return self._post(
            "/memory/drop",
            body=maybe_transform({"bank_id": bank_id}, memory_drop_params.MemoryDropParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    def insert(
        self,
        *,
        bank_id: str,
        documents: Iterable[memory_insert_params.Document],
        ttl_seconds: int | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._post(
            "/memory/insert",
            body=maybe_transform(
                {
                    "bank_id": bank_id,
                    "documents": documents,
                    "ttl_seconds": ttl_seconds,
                },
                memory_insert_params.MemoryInsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def query(
        self,
        *,
        bank_id: str,
        query: memory_query_params.Query,
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryDocuments:
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
        return self._post(
            "/memory/query",
            body=maybe_transform(
                {
                    "bank_id": bank_id,
                    "query": query,
                    "params": params,
                },
                memory_query_params.MemoryQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryDocuments,
        )


class AsyncMemoryResource(AsyncAPIResource):
    @cached_property
    def documents(self) -> AsyncDocumentsResource:
        return AsyncDocumentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncMemoryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: memory_create_params.Config,
        name: str,
        url: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryCreateResponse:
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
        return await self._post(
            "/memory/create",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                    "url": url,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryCreateResponse,
        )

    async def retrieve(
        self,
        *,
        bank_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MemoryRetrieveResponse]:
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
            "/memory/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"bank_id": bank_id}, memory_retrieve_params.MemoryRetrieveParams),
            ),
            cast_to=MemoryRetrieveResponse,
        )

    async def update(
        self,
        *,
        bank_id: str,
        documents: Iterable[memory_update_params.Document],
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/memory/update",
            body=await async_maybe_transform(
                {
                    "bank_id": bank_id,
                    "documents": documents,
                },
                memory_update_params.MemoryUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        *,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MemoryListResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._get(
            "/memory/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryListResponse,
        )

    async def drop(
        self,
        *,
        bank_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> str:
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
        return await self._post(
            "/memory/drop",
            body=await async_maybe_transform({"bank_id": bank_id}, memory_drop_params.MemoryDropParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
        )

    async def insert(
        self,
        *,
        bank_id: str,
        documents: Iterable[memory_insert_params.Document],
        ttl_seconds: int | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/memory/insert",
            body=await async_maybe_transform(
                {
                    "bank_id": bank_id,
                    "documents": documents,
                    "ttl_seconds": ttl_seconds,
                },
                memory_insert_params.MemoryInsertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def query(
        self,
        *,
        bank_id: str,
        query: memory_query_params.Query,
        params: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> QueryDocuments:
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
        return await self._post(
            "/memory/query",
            body=await async_maybe_transform(
                {
                    "bank_id": bank_id,
                    "query": query,
                    "params": params,
                },
                memory_query_params.MemoryQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryDocuments,
        )


class MemoryResourceWithRawResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.create = to_raw_response_wrapper(
            memory.create,
        )
        self.retrieve = to_raw_response_wrapper(
            memory.retrieve,
        )
        self.update = to_raw_response_wrapper(
            memory.update,
        )
        self.list = to_raw_response_wrapper(
            memory.list,
        )
        self.drop = to_raw_response_wrapper(
            memory.drop,
        )
        self.insert = to_raw_response_wrapper(
            memory.insert,
        )
        self.query = to_raw_response_wrapper(
            memory.query,
        )

    @cached_property
    def documents(self) -> DocumentsResourceWithRawResponse:
        return DocumentsResourceWithRawResponse(self._memory.documents)


class AsyncMemoryResourceWithRawResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.create = async_to_raw_response_wrapper(
            memory.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            memory.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            memory.update,
        )
        self.list = async_to_raw_response_wrapper(
            memory.list,
        )
        self.drop = async_to_raw_response_wrapper(
            memory.drop,
        )
        self.insert = async_to_raw_response_wrapper(
            memory.insert,
        )
        self.query = async_to_raw_response_wrapper(
            memory.query,
        )

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithRawResponse:
        return AsyncDocumentsResourceWithRawResponse(self._memory.documents)


class MemoryResourceWithStreamingResponse:
    def __init__(self, memory: MemoryResource) -> None:
        self._memory = memory

        self.create = to_streamed_response_wrapper(
            memory.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            memory.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            memory.update,
        )
        self.list = to_streamed_response_wrapper(
            memory.list,
        )
        self.drop = to_streamed_response_wrapper(
            memory.drop,
        )
        self.insert = to_streamed_response_wrapper(
            memory.insert,
        )
        self.query = to_streamed_response_wrapper(
            memory.query,
        )

    @cached_property
    def documents(self) -> DocumentsResourceWithStreamingResponse:
        return DocumentsResourceWithStreamingResponse(self._memory.documents)


class AsyncMemoryResourceWithStreamingResponse:
    def __init__(self, memory: AsyncMemoryResource) -> None:
        self._memory = memory

        self.create = async_to_streamed_response_wrapper(
            memory.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            memory.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            memory.update,
        )
        self.list = async_to_streamed_response_wrapper(
            memory.list,
        )
        self.drop = async_to_streamed_response_wrapper(
            memory.drop,
        )
        self.insert = async_to_streamed_response_wrapper(
            memory.insert,
        )
        self.query = async_to_streamed_response_wrapper(
            memory.query,
        )

    @cached_property
    def documents(self) -> AsyncDocumentsResourceWithStreamingResponse:
        return AsyncDocumentsResourceWithStreamingResponse(self._memory.documents)

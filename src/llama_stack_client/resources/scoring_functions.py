# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    ScoringFnDefWithProvider,
    scoring_function_register_params,
    scoring_function_retrieve_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.scoring_fn_def_with_provider import ScoringFnDefWithProvider
from ..types.scoring_fn_def_with_provider_param import ScoringFnDefWithProviderParam

__all__ = ["ScoringFunctionsResource", "AsyncScoringFunctionsResource"]


class ScoringFunctionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScoringFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return ScoringFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScoringFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return ScoringFunctionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        name: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScoringFnDefWithProvider]:
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
            "/scoring_functions/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, scoring_function_retrieve_params.ScoringFunctionRetrieveParams),
            ),
            cast_to=ScoringFnDefWithProvider,
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
    ) -> ScoringFnDefWithProvider:
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
            "/scoring_functions/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringFnDefWithProvider,
        )

    def register(
        self,
        *,
        function_def: ScoringFnDefWithProviderParam,
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
            "/scoring_functions/register",
            body=maybe_transform(
                {"function_def": function_def}, scoring_function_register_params.ScoringFunctionRegisterParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncScoringFunctionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScoringFunctionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScoringFunctionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScoringFunctionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncScoringFunctionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        name: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ScoringFnDefWithProvider]:
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
            "/scoring_functions/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"name": name}, scoring_function_retrieve_params.ScoringFunctionRetrieveParams
                ),
            ),
            cast_to=ScoringFnDefWithProvider,
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
    ) -> ScoringFnDefWithProvider:
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
            "/scoring_functions/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScoringFnDefWithProvider,
        )

    async def register(
        self,
        *,
        function_def: ScoringFnDefWithProviderParam,
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
            "/scoring_functions/register",
            body=await async_maybe_transform(
                {"function_def": function_def}, scoring_function_register_params.ScoringFunctionRegisterParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ScoringFunctionsResourceWithRawResponse:
    def __init__(self, scoring_functions: ScoringFunctionsResource) -> None:
        self._scoring_functions = scoring_functions

        self.retrieve = to_raw_response_wrapper(
            scoring_functions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            scoring_functions.list,
        )
        self.register = to_raw_response_wrapper(
            scoring_functions.register,
        )


class AsyncScoringFunctionsResourceWithRawResponse:
    def __init__(self, scoring_functions: AsyncScoringFunctionsResource) -> None:
        self._scoring_functions = scoring_functions

        self.retrieve = async_to_raw_response_wrapper(
            scoring_functions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            scoring_functions.list,
        )
        self.register = async_to_raw_response_wrapper(
            scoring_functions.register,
        )


class ScoringFunctionsResourceWithStreamingResponse:
    def __init__(self, scoring_functions: ScoringFunctionsResource) -> None:
        self._scoring_functions = scoring_functions

        self.retrieve = to_streamed_response_wrapper(
            scoring_functions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            scoring_functions.list,
        )
        self.register = to_streamed_response_wrapper(
            scoring_functions.register,
        )


class AsyncScoringFunctionsResourceWithStreamingResponse:
    def __init__(self, scoring_functions: AsyncScoringFunctionsResource) -> None:
        self._scoring_functions = scoring_functions

        self.retrieve = async_to_streamed_response_wrapper(
            scoring_functions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            scoring_functions.list,
        )
        self.register = async_to_streamed_response_wrapper(
            scoring_functions.register,
        )

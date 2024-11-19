# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional

import httpx

from ..types import eval_task_register_params, eval_task_retrieve_params
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
from ..types.eval_task import EvalTask

__all__ = ["EvalTasksResource", "AsyncEvalTasksResource"]


class EvalTasksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvalTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return EvalTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return EvalTasksResourceWithStreamingResponse(self)

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
    ) -> Optional[EvalTask]:
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
            "/alpha/eval-tasks/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"name": name}, eval_task_retrieve_params.EvalTaskRetrieveParams),
            ),
            cast_to=EvalTask,
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
    ) -> EvalTask:
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
            "/alpha/eval-tasks/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalTask,
        )

    def register(
        self,
        *,
        dataset_id: str,
        eval_task_id: str,
        scoring_functions: List[str],
        metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_eval_task_id: str | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
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
            "/alpha/eval-tasks/register",
            body=maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "eval_task_id": eval_task_id,
                    "scoring_functions": scoring_functions,
                    "metadata": metadata,
                    "provider_eval_task_id": provider_eval_task_id,
                    "provider_id": provider_id,
                },
                eval_task_register_params.EvalTaskRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEvalTasksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvalTasksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalTasksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalTasksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncEvalTasksResourceWithStreamingResponse(self)

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
    ) -> Optional[EvalTask]:
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
            "/alpha/eval-tasks/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"name": name}, eval_task_retrieve_params.EvalTaskRetrieveParams),
            ),
            cast_to=EvalTask,
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
    ) -> EvalTask:
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
            "/alpha/eval-tasks/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvalTask,
        )

    async def register(
        self,
        *,
        dataset_id: str,
        eval_task_id: str,
        scoring_functions: List[str],
        metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        provider_eval_task_id: str | NotGiven = NOT_GIVEN,
        provider_id: str | NotGiven = NOT_GIVEN,
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
            "/alpha/eval-tasks/register",
            body=await async_maybe_transform(
                {
                    "dataset_id": dataset_id,
                    "eval_task_id": eval_task_id,
                    "scoring_functions": scoring_functions,
                    "metadata": metadata,
                    "provider_eval_task_id": provider_eval_task_id,
                    "provider_id": provider_id,
                },
                eval_task_register_params.EvalTaskRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EvalTasksResourceWithRawResponse:
    def __init__(self, eval_tasks: EvalTasksResource) -> None:
        self._eval_tasks = eval_tasks

        self.retrieve = to_raw_response_wrapper(
            eval_tasks.retrieve,
        )
        self.list = to_raw_response_wrapper(
            eval_tasks.list,
        )
        self.register = to_raw_response_wrapper(
            eval_tasks.register,
        )


class AsyncEvalTasksResourceWithRawResponse:
    def __init__(self, eval_tasks: AsyncEvalTasksResource) -> None:
        self._eval_tasks = eval_tasks

        self.retrieve = async_to_raw_response_wrapper(
            eval_tasks.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            eval_tasks.list,
        )
        self.register = async_to_raw_response_wrapper(
            eval_tasks.register,
        )


class EvalTasksResourceWithStreamingResponse:
    def __init__(self, eval_tasks: EvalTasksResource) -> None:
        self._eval_tasks = eval_tasks

        self.retrieve = to_streamed_response_wrapper(
            eval_tasks.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            eval_tasks.list,
        )
        self.register = to_streamed_response_wrapper(
            eval_tasks.register,
        )


class AsyncEvalTasksResourceWithStreamingResponse:
    def __init__(self, eval_tasks: AsyncEvalTasksResource) -> None:
        self._eval_tasks = eval_tasks

        self.retrieve = async_to_streamed_response_wrapper(
            eval_tasks.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            eval_tasks.list,
        )
        self.register = async_to_streamed_response_wrapper(
            eval_tasks.register,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ...types import eval_run_eval_params, eval_evaluate_rows_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    strip_not_given,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.job import Job
from ..._base_client import make_request_options
from ...types.evaluate_response import EvaluateResponse

__all__ = ["EvalResource", "AsyncEvalResource"]


class EvalResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return EvalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return EvalResourceWithStreamingResponse(self)

    def evaluate_rows(
        self,
        *,
        input_rows: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]],
        scoring_functions: List[str],
        task_config: eval_evaluate_rows_params.TaskConfig,
        task_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
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
            "/alpha/eval/evaluate-rows",
            body=maybe_transform(
                {
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                    "task_config": task_config,
                    "task_id": task_id,
                },
                eval_evaluate_rows_params.EvalEvaluateRowsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    def run_eval(
        self,
        *,
        task_config: eval_run_eval_params.TaskConfig,
        task_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Job:
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
            "/alpha/eval/run-eval",
            body=maybe_transform(
                {
                    "task_config": task_config,
                    "task_id": task_id,
                },
                eval_run_eval_params.EvalRunEvalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class AsyncEvalResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncEvalResourceWithStreamingResponse(self)

    async def evaluate_rows(
        self,
        *,
        input_rows: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]],
        scoring_functions: List[str],
        task_config: eval_evaluate_rows_params.TaskConfig,
        task_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
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
            "/alpha/eval/evaluate-rows",
            body=await async_maybe_transform(
                {
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                    "task_config": task_config,
                    "task_id": task_id,
                },
                eval_evaluate_rows_params.EvalEvaluateRowsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    async def run_eval(
        self,
        *,
        task_config: eval_run_eval_params.TaskConfig,
        task_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Job:
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
            "/alpha/eval/run-eval",
            body=await async_maybe_transform(
                {
                    "task_config": task_config,
                    "task_id": task_id,
                },
                eval_run_eval_params.EvalRunEvalParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class EvalResourceWithRawResponse:
    def __init__(self, eval: EvalResource) -> None:
        self._eval = eval

        self.evaluate_rows = to_raw_response_wrapper(
            eval.evaluate_rows,
        )
        self.run_eval = to_raw_response_wrapper(
            eval.run_eval,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._eval.jobs)


class AsyncEvalResourceWithRawResponse:
    def __init__(self, eval: AsyncEvalResource) -> None:
        self._eval = eval

        self.evaluate_rows = async_to_raw_response_wrapper(
            eval.evaluate_rows,
        )
        self.run_eval = async_to_raw_response_wrapper(
            eval.run_eval,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._eval.jobs)


class EvalResourceWithStreamingResponse:
    def __init__(self, eval: EvalResource) -> None:
        self._eval = eval

        self.evaluate_rows = to_streamed_response_wrapper(
            eval.evaluate_rows,
        )
        self.run_eval = to_streamed_response_wrapper(
            eval.run_eval,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._eval.jobs)


class AsyncEvalResourceWithStreamingResponse:
    def __init__(self, eval: AsyncEvalResource) -> None:
        self._eval = eval

        self.evaluate_rows = async_to_streamed_response_wrapper(
            eval.evaluate_rows,
        )
        self.run_eval = async_to_streamed_response_wrapper(
            eval.run_eval,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._eval.jobs)

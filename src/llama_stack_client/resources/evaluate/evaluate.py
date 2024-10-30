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
from ...types import evaluate_evaluate_params, evaluate_evaluate_batch_params
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
from ...types.evaluate.evaluate_response import EvaluateResponse

__all__ = ["EvaluateResource", "AsyncEvaluateResource"]


class EvaluateResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return EvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return EvaluateResourceWithStreamingResponse(self)

    def evaluate(
        self,
        *,
        candidate: evaluate_evaluate_params.Candidate,
        input_rows: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]],
        scoring_functions: List[str],
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
            "/eval/evaluate",
            body=maybe_transform(
                {
                    "candidate": candidate,
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                evaluate_evaluate_params.EvaluateEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    def evaluate_batch(
        self,
        *,
        candidate: evaluate_evaluate_batch_params.Candidate,
        dataset_id: str,
        scoring_functions: List[str],
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
            "/eval/evaluate_batch",
            body=maybe_transform(
                {
                    "candidate": candidate,
                    "dataset_id": dataset_id,
                    "scoring_functions": scoring_functions,
                },
                evaluate_evaluate_batch_params.EvaluateEvaluateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class AsyncEvaluateResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvaluateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncEvaluateResourceWithStreamingResponse(self)

    async def evaluate(
        self,
        *,
        candidate: evaluate_evaluate_params.Candidate,
        input_rows: Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]],
        scoring_functions: List[str],
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
            "/eval/evaluate",
            body=await async_maybe_transform(
                {
                    "candidate": candidate,
                    "input_rows": input_rows,
                    "scoring_functions": scoring_functions,
                },
                evaluate_evaluate_params.EvaluateEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    async def evaluate_batch(
        self,
        *,
        candidate: evaluate_evaluate_batch_params.Candidate,
        dataset_id: str,
        scoring_functions: List[str],
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
            "/eval/evaluate_batch",
            body=await async_maybe_transform(
                {
                    "candidate": candidate,
                    "dataset_id": dataset_id,
                    "scoring_functions": scoring_functions,
                },
                evaluate_evaluate_batch_params.EvaluateEvaluateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Job,
        )


class EvaluateResourceWithRawResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.evaluate = to_raw_response_wrapper(
            evaluate.evaluate,
        )
        self.evaluate_batch = to_raw_response_wrapper(
            evaluate.evaluate_batch,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._evaluate.jobs)


class AsyncEvaluateResourceWithRawResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.evaluate = async_to_raw_response_wrapper(
            evaluate.evaluate,
        )
        self.evaluate_batch = async_to_raw_response_wrapper(
            evaluate.evaluate_batch,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._evaluate.jobs)


class EvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

        self.evaluate = to_streamed_response_wrapper(
            evaluate.evaluate,
        )
        self.evaluate_batch = to_streamed_response_wrapper(
            evaluate.evaluate_batch,
        )

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._evaluate.jobs)


class AsyncEvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

        self.evaluate = async_to_streamed_response_wrapper(
            evaluate.evaluate,
        )
        self.evaluate_batch = async_to_streamed_response_wrapper(
            evaluate.evaluate_batch,
        )

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._evaluate.jobs)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

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
from ..._base_client import make_request_options
from ...types.evaluate import question_answering_create_params
from ...types.evaluation_job import EvaluationJob

__all__ = ["QuestionAnsweringResource", "AsyncQuestionAnsweringResource"]


class QuestionAnsweringResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QuestionAnsweringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return QuestionAnsweringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QuestionAnsweringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return QuestionAnsweringResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        metrics: List[Literal["em", "f1"]],
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationJob:
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
            "/evaluate/question_answering/",
            body=maybe_transform({"metrics": metrics}, question_answering_create_params.QuestionAnsweringCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationJob,
        )


class AsyncQuestionAnsweringResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQuestionAnsweringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQuestionAnsweringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQuestionAnsweringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncQuestionAnsweringResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        metrics: List[Literal["em", "f1"]],
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationJob:
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
            "/evaluate/question_answering/",
            body=await async_maybe_transform(
                {"metrics": metrics}, question_answering_create_params.QuestionAnsweringCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationJob,
        )


class QuestionAnsweringResourceWithRawResponse:
    def __init__(self, question_answering: QuestionAnsweringResource) -> None:
        self._question_answering = question_answering

        self.create = to_raw_response_wrapper(
            question_answering.create,
        )


class AsyncQuestionAnsweringResourceWithRawResponse:
    def __init__(self, question_answering: AsyncQuestionAnsweringResource) -> None:
        self._question_answering = question_answering

        self.create = async_to_raw_response_wrapper(
            question_answering.create,
        )


class QuestionAnsweringResourceWithStreamingResponse:
    def __init__(self, question_answering: QuestionAnsweringResource) -> None:
        self._question_answering = question_answering

        self.create = to_streamed_response_wrapper(
            question_answering.create,
        )


class AsyncQuestionAnsweringResourceWithStreamingResponse:
    def __init__(self, question_answering: AsyncQuestionAnsweringResource) -> None:
        self._question_answering = question_answering

        self.create = async_to_streamed_response_wrapper(
            question_answering.create,
        )

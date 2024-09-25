# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .jobs.jobs import JobsResource, AsyncJobsResource
from ..._resource import SyncAPIResource, AsyncAPIResource
from .question_answering import (
    QuestionAnsweringResource,
    AsyncQuestionAnsweringResource,
    QuestionAnsweringResourceWithRawResponse,
    AsyncQuestionAnsweringResourceWithRawResponse,
    QuestionAnsweringResourceWithStreamingResponse,
    AsyncQuestionAnsweringResourceWithStreamingResponse,
)

__all__ = ["EvaluateResource", "AsyncEvaluateResource"]


class EvaluateResource(SyncAPIResource):
    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def question_answering(self) -> QuestionAnsweringResource:
        return QuestionAnsweringResource(self._client)

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


class AsyncEvaluateResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def question_answering(self) -> AsyncQuestionAnsweringResource:
        return AsyncQuestionAnsweringResource(self._client)

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


class EvaluateResourceWithRawResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._evaluate.jobs)

    @cached_property
    def question_answering(self) -> QuestionAnsweringResourceWithRawResponse:
        return QuestionAnsweringResourceWithRawResponse(self._evaluate.question_answering)


class AsyncEvaluateResourceWithRawResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._evaluate.jobs)

    @cached_property
    def question_answering(self) -> AsyncQuestionAnsweringResourceWithRawResponse:
        return AsyncQuestionAnsweringResourceWithRawResponse(self._evaluate.question_answering)


class EvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: EvaluateResource) -> None:
        self._evaluate = evaluate

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._evaluate.jobs)

    @cached_property
    def question_answering(self) -> QuestionAnsweringResourceWithStreamingResponse:
        return QuestionAnsweringResourceWithStreamingResponse(self._evaluate.question_answering)


class AsyncEvaluateResourceWithStreamingResponse:
    def __init__(self, evaluate: AsyncEvaluateResource) -> None:
        self._evaluate = evaluate

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._evaluate.jobs)

    @cached_property
    def question_answering(self) -> AsyncQuestionAnsweringResourceWithStreamingResponse:
        return AsyncQuestionAnsweringResourceWithStreamingResponse(self._evaluate.question_answering)

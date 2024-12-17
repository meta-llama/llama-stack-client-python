# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Union

import httpx

from llama_stack_client.types import (
    post_training_get_training_job_artifacts_params,
    post_training_get_training_job_status_params,
)
from typing_extensions import Literal

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import Body, Headers, NOT_GIVEN, NotGiven, Query
from ..._utils import async_maybe_transform, maybe_transform, strip_not_given
from ...types import (
    post_training_preference_optimize_params,
    post_training_supervised_fine_tune_params,
)
from ...types.post_training.post_training_job_artifacts import PostTrainingJobArtifacts
from ...types.post_training.post_training_job_status import PostTrainingJobStatus
from ...types.post_training_job import PostTrainingJob

from .job import (
    AsyncJobResource,
    AsyncJobResourceWithRawResponse,
    AsyncJobResourceWithStreamingResponse,
    JobResource,
    JobResourceWithRawResponse,
    JobResourceWithStreamingResponse,
)

__all__ = ["PostTrainingResource", "AsyncPostTrainingResource"]


class PostTrainingResource(SyncAPIResource):
    @cached_property
    def job(self) -> JobResource:
        return JobResource(self._client)

    @cached_property
    def with_raw_response(self) -> PostTrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return PostTrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PostTrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return PostTrainingResourceWithStreamingResponse(self)

    def preference_optimize(
        self,
        *,
        algorithm_config: post_training_preference_optimize_params.AlgorithmConfig,
        finetuned_model: str,
        hyperparam_search_config: Dict[
            str, Union[bool, float, str, Iterable[object], object, None]
        ],
        job_uuid: str,
        logger_config: Dict[
            str, Union[bool, float, str, Iterable[object], object, None]
        ],
        training_config: post_training_preference_optimize_params.TrainingConfig,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {"X-LlamaStack-ProviderData": x_llama_stack_provider_data}
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/alpha/post-training/preference-optimize",
            body=maybe_transform(
                {
                    "algorithm_config": algorithm_config,
                    "finetuned_model": finetuned_model,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "training_config": training_config,
                },
                post_training_preference_optimize_params.PostTrainingPreferenceOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostTrainingJob,
        )

    def supervised_fine_tune(
        self,
        *,
        hyperparam_search_config: Dict[
            str, Union[bool, float, str, Iterable[object], object, None]
        ],
        job_uuid: str,
        logger_config: Dict[
            str, Union[bool, float, str, Iterable[object], object, None]
        ],
        model: str,
        training_config: post_training_supervised_fine_tune_params.TrainingConfig,
        algorithm_config: (
            post_training_supervised_fine_tune_params.AlgorithmConfig | NotGiven
        ) = NOT_GIVEN,
        checkpoint_dir: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {"X-LlamaStack-ProviderData": x_llama_stack_provider_data}
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/alpha/post-training/supervised-fine-tune",
            body=maybe_transform(
                {
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "model": model,
                    "training_config": training_config,
                    "algorithm_config": algorithm_config,
                    "checkpoint_dir": checkpoint_dir,
                },
                post_training_supervised_fine_tune_params.PostTrainingSupervisedFineTuneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostTrainingJob,
        )

    def get_training_jobs(
        self,
        *,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {"X-LlamaStack-ProviderData": x_llama_stack_provider_data}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/alpha/post-training/jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostTrainingJob,
        )

    def get_training_job_status(
        self,
        *,
        job_uuid: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJobStatus:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {"X-LlamaStack-ProviderData": x_llama_stack_provider_data}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/alpha/post-training/job/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"job_uuid": job_uuid},
                    post_training_get_training_job_status_params.PostTrainingGetTrainingJobStatusParams,
                ),
            ),
            cast_to=PostTrainingJobStatus,
        )

    def get_training_job_artifacts(
        self,
        *,
        job_uuid: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJobArtifacts:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {"X-LlamaStack-ProviderData": x_llama_stack_provider_data}
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/alpha/post-training/job/artifacts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"job_uuid": job_uuid},
                    post_training_get_training_job_artifacts_params.PostTrainingGetTrainingJobArtifactsParams,
                ),
            ),
            cast_to=PostTrainingJobArtifacts,
        )


class AsyncPostTrainingResource(AsyncAPIResource):
    @cached_property
    def job(self) -> AsyncJobResource:
        return AsyncJobResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPostTrainingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPostTrainingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPostTrainingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncPostTrainingResourceWithStreamingResponse(self)

    async def preference_optimize(
        self,
        *,
        algorithm_config: post_training_preference_optimize_params.AlgorithmConfig,
        finetuned_model: str,
        hyperparam_search_config: Dict[
            str, Union[bool, float, str, Iterable[object], object, None]
        ],
        job_uuid: str,
        logger_config: Dict[
            str, Union[bool, float, str, Iterable[object], object, None]
        ],
        training_config: post_training_preference_optimize_params.TrainingConfig,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {"X-LlamaStack-ProviderData": x_llama_stack_provider_data}
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/alpha/post-training/preference-optimize",
            body=await async_maybe_transform(
                {
                    "algorithm_config": algorithm_config,
                    "finetuned_model": finetuned_model,
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "training_config": training_config,
                },
                post_training_preference_optimize_params.PostTrainingPreferenceOptimizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostTrainingJob,
        )

    async def supervised_fine_tune(
        self,
        *,
        hyperparam_search_config: Dict[
            str, Union[bool, float, str, Iterable[object], object, None]
        ],
        job_uuid: str,
        logger_config: Dict[
            str, Union[bool, float, str, Iterable[object], object, None]
        ],
        model: str,
        training_config: post_training_supervised_fine_tune_params.TrainingConfig,
        algorithm_config: (
            post_training_supervised_fine_tune_params.AlgorithmConfig | NotGiven
        ) = NOT_GIVEN,
        checkpoint_dir: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PostTrainingJob:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {"X-LlamaStack-ProviderData": x_llama_stack_provider_data}
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/alpha/post-training/supervised-fine-tune",
            body=await async_maybe_transform(
                {
                    "hyperparam_search_config": hyperparam_search_config,
                    "job_uuid": job_uuid,
                    "logger_config": logger_config,
                    "model": model,
                    "training_config": training_config,
                    "algorithm_config": algorithm_config,
                    "checkpoint_dir": checkpoint_dir,
                },
                post_training_supervised_fine_tune_params.PostTrainingSupervisedFineTuneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=PostTrainingJob,
        )


class PostTrainingResourceWithRawResponse:
    def __init__(self, post_training: PostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = to_raw_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = to_raw_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def job(self) -> JobResourceWithRawResponse:
        return JobResourceWithRawResponse(self._post_training.job)


class AsyncPostTrainingResourceWithRawResponse:
    def __init__(self, post_training: AsyncPostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = async_to_raw_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = async_to_raw_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithRawResponse:
        return AsyncJobResourceWithRawResponse(self._post_training.job)


class PostTrainingResourceWithStreamingResponse:
    def __init__(self, post_training: PostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = to_streamed_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = to_streamed_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def job(self) -> JobResourceWithStreamingResponse:
        return JobResourceWithStreamingResponse(self._post_training.job)


class AsyncPostTrainingResourceWithStreamingResponse:
    def __init__(self, post_training: AsyncPostTrainingResource) -> None:
        self._post_training = post_training

        self.preference_optimize = async_to_streamed_response_wrapper(
            post_training.preference_optimize,
        )
        self.supervised_fine_tune = async_to_streamed_response_wrapper(
            post_training.supervised_fine_tune,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithStreamingResponse:
        return AsyncJobResourceWithStreamingResponse(self._post_training.job)

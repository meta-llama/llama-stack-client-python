# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import batch_inference_completion_params, batch_inference_chat_completion_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
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
from ..types.shared_params.message import Message
from ..types.shared.batch_completion import BatchCompletion
from ..types.shared_params.response_format import ResponseFormat
from ..types.shared_params.sampling_params import SamplingParams
from ..types.shared_params.interleaved_content import InterleavedContent
from ..types.batch_inference_chat_completion_response import BatchInferenceChatCompletionResponse

__all__ = ["BatchInferenceResource", "AsyncBatchInferenceResource"]


class BatchInferenceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchInferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return BatchInferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchInferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return BatchInferenceResourceWithStreamingResponse(self)

    def chat_completion(
        self,
        *,
        messages_batch: Iterable[Iterable[Message]],
        model: str,
        logprobs: batch_inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[batch_inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchInferenceChatCompletionResponse:
        """
        Args:
          response_format: Configuration for JSON schema-guided response generation.

          tool_choice: Whether tool use is required or automatic. This is a hint to the model which may
              not be followed. It depends on the Instruction Following capabilities of the
              model.

          tool_prompt_format: Prompt format for calling custom / zero shot tools.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/batch-inference/chat-completion",
            body=maybe_transform(
                {
                    "messages_batch": messages_batch,
                    "model": model,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                    "tool_choice": tool_choice,
                    "tool_prompt_format": tool_prompt_format,
                    "tools": tools,
                },
                batch_inference_chat_completion_params.BatchInferenceChatCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchInferenceChatCompletionResponse,
        )

    def completion(
        self,
        *,
        content_batch: List[InterleavedContent],
        model: str,
        logprobs: batch_inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCompletion:
        """
        Args:
          response_format: Configuration for JSON schema-guided response generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/batch-inference/completion",
            body=maybe_transform(
                {
                    "content_batch": content_batch,
                    "model": model,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                },
                batch_inference_completion_params.BatchInferenceCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCompletion,
        )


class AsyncBatchInferenceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchInferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchInferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchInferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncBatchInferenceResourceWithStreamingResponse(self)

    async def chat_completion(
        self,
        *,
        messages_batch: Iterable[Iterable[Message]],
        model: str,
        logprobs: batch_inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required", "none"] | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[batch_inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchInferenceChatCompletionResponse:
        """
        Args:
          response_format: Configuration for JSON schema-guided response generation.

          tool_choice: Whether tool use is required or automatic. This is a hint to the model which may
              not be followed. It depends on the Instruction Following capabilities of the
              model.

          tool_prompt_format: Prompt format for calling custom / zero shot tools.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/batch-inference/chat-completion",
            body=await async_maybe_transform(
                {
                    "messages_batch": messages_batch,
                    "model": model,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                    "tool_choice": tool_choice,
                    "tool_prompt_format": tool_prompt_format,
                    "tools": tools,
                },
                batch_inference_chat_completion_params.BatchInferenceChatCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchInferenceChatCompletionResponse,
        )

    async def completion(
        self,
        *,
        content_batch: List[InterleavedContent],
        model: str,
        logprobs: batch_inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCompletion:
        """
        Args:
          response_format: Configuration for JSON schema-guided response generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/batch-inference/completion",
            body=await async_maybe_transform(
                {
                    "content_batch": content_batch,
                    "model": model,
                    "logprobs": logprobs,
                    "response_format": response_format,
                    "sampling_params": sampling_params,
                },
                batch_inference_completion_params.BatchInferenceCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCompletion,
        )


class BatchInferenceResourceWithRawResponse:
    def __init__(self, batch_inference: BatchInferenceResource) -> None:
        self._batch_inference = batch_inference

        self.chat_completion = to_raw_response_wrapper(
            batch_inference.chat_completion,
        )
        self.completion = to_raw_response_wrapper(
            batch_inference.completion,
        )


class AsyncBatchInferenceResourceWithRawResponse:
    def __init__(self, batch_inference: AsyncBatchInferenceResource) -> None:
        self._batch_inference = batch_inference

        self.chat_completion = async_to_raw_response_wrapper(
            batch_inference.chat_completion,
        )
        self.completion = async_to_raw_response_wrapper(
            batch_inference.completion,
        )


class BatchInferenceResourceWithStreamingResponse:
    def __init__(self, batch_inference: BatchInferenceResource) -> None:
        self._batch_inference = batch_inference

        self.chat_completion = to_streamed_response_wrapper(
            batch_inference.chat_completion,
        )
        self.completion = to_streamed_response_wrapper(
            batch_inference.completion,
        )


class AsyncBatchInferenceResourceWithStreamingResponse:
    def __init__(self, batch_inference: AsyncBatchInferenceResource) -> None:
        self._batch_inference = batch_inference

        self.chat_completion = async_to_streamed_response_wrapper(
            batch_inference.chat_completion,
        )
        self.completion = async_to_streamed_response_wrapper(
            batch_inference.completion,
        )

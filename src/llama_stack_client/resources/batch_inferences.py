# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal

import httpx

from ..types import batch_inference_completion_params, batch_inference_chat_completion_params
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
from ..types.shared.batch_completion import BatchCompletion
from ..types.shared_params.sampling_params import SamplingParams
from ..types.batch_inference_chat_completion_response import BatchInferenceChatCompletionResponse

__all__ = ["BatchInferencesResource", "AsyncBatchInferencesResource"]


class BatchInferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchInferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return BatchInferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchInferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return BatchInferencesResourceWithStreamingResponse(self)

    def chat_completion(
        self,
        *,
        messages_batch: Iterable[Iterable[batch_inference_chat_completion_params.MessagesBatch]],
        model: str,
        logprobs: batch_inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required"] | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[batch_inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchInferenceChatCompletionResponse:
        """
        Args:
          tool_prompt_format: `json` -- Refers to the json format for calling tools. The json format takes the
              form like { "type": "function", "function" : { "name": "function_name",
              "description": "function_description", "parameters": {...} } }

              `function_tag` -- This is an example of how you could define your own user
              defined format for making tool calls. The function_tag format looks like this,
              <function=function_name>(parameters)</function>

              The detailed prompts for each of these formats are added to llama cli

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
            "/batch_inference/chat_completion",
            body=maybe_transform(
                {
                    "messages_batch": messages_batch,
                    "model": model,
                    "logprobs": logprobs,
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
        content_batch: List[batch_inference_completion_params.ContentBatch],
        model: str,
        logprobs: batch_inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCompletion:
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
            "/batch_inference/completion",
            body=maybe_transform(
                {
                    "content_batch": content_batch,
                    "model": model,
                    "logprobs": logprobs,
                    "sampling_params": sampling_params,
                },
                batch_inference_completion_params.BatchInferenceCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCompletion,
        )


class AsyncBatchInferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchInferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchInferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchInferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncBatchInferencesResourceWithStreamingResponse(self)

    async def chat_completion(
        self,
        *,
        messages_batch: Iterable[Iterable[batch_inference_chat_completion_params.MessagesBatch]],
        model: str,
        logprobs: batch_inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required"] | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[batch_inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchInferenceChatCompletionResponse:
        """
        Args:
          tool_prompt_format: `json` -- Refers to the json format for calling tools. The json format takes the
              form like { "type": "function", "function" : { "name": "function_name",
              "description": "function_description", "parameters": {...} } }

              `function_tag` -- This is an example of how you could define your own user
              defined format for making tool calls. The function_tag format looks like this,
              <function=function_name>(parameters)</function>

              The detailed prompts for each of these formats are added to llama cli

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
            "/batch_inference/chat_completion",
            body=await async_maybe_transform(
                {
                    "messages_batch": messages_batch,
                    "model": model,
                    "logprobs": logprobs,
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
        content_batch: List[batch_inference_completion_params.ContentBatch],
        model: str,
        logprobs: batch_inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BatchCompletion:
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
            "/batch_inference/completion",
            body=await async_maybe_transform(
                {
                    "content_batch": content_batch,
                    "model": model,
                    "logprobs": logprobs,
                    "sampling_params": sampling_params,
                },
                batch_inference_completion_params.BatchInferenceCompletionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCompletion,
        )


class BatchInferencesResourceWithRawResponse:
    def __init__(self, batch_inferences: BatchInferencesResource) -> None:
        self._batch_inferences = batch_inferences

        self.chat_completion = to_raw_response_wrapper(
            batch_inferences.chat_completion,
        )
        self.completion = to_raw_response_wrapper(
            batch_inferences.completion,
        )


class AsyncBatchInferencesResourceWithRawResponse:
    def __init__(self, batch_inferences: AsyncBatchInferencesResource) -> None:
        self._batch_inferences = batch_inferences

        self.chat_completion = async_to_raw_response_wrapper(
            batch_inferences.chat_completion,
        )
        self.completion = async_to_raw_response_wrapper(
            batch_inferences.completion,
        )


class BatchInferencesResourceWithStreamingResponse:
    def __init__(self, batch_inferences: BatchInferencesResource) -> None:
        self._batch_inferences = batch_inferences

        self.chat_completion = to_streamed_response_wrapper(
            batch_inferences.chat_completion,
        )
        self.completion = to_streamed_response_wrapper(
            batch_inferences.completion,
        )


class AsyncBatchInferencesResourceWithStreamingResponse:
    def __init__(self, batch_inferences: AsyncBatchInferencesResource) -> None:
        self._batch_inferences = batch_inferences

        self.chat_completion = async_to_streamed_response_wrapper(
            batch_inferences.chat_completion,
        )
        self.completion = async_to_streamed_response_wrapper(
            batch_inferences.completion,
        )

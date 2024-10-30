# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Iterable, cast
from typing_extensions import Literal

import httpx

from ..types import (
    inference_completion_params,
    inference_embeddings_params,
    inference_chat_completion_params,
)
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
from ..types.embeddings_response import EmbeddingsResponse
from ..types.inference_completion_response import InferenceCompletionResponse
from ..types.shared_params.sampling_params import SamplingParams
from ..types.inference_chat_completion_response import InferenceChatCompletionResponse

__all__ = ["InferenceResource", "AsyncInferenceResource"]


class InferenceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return InferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return InferenceResourceWithStreamingResponse(self)

    def chat_completion(
        self,
        *,
        messages: Iterable[inference_chat_completion_params.Message],
        model: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required"] | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceChatCompletionResponse:
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
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return cast(
            InferenceChatCompletionResponse,
            self._post(
                "/inference/chat_completion",
                body=maybe_transform(
                    {
                        "messages": messages,
                        "model": model,
                        "logprobs": logprobs,
                        "response_format": response_format,
                        "sampling_params": sampling_params,
                        "stream": stream,
                        "tool_choice": tool_choice,
                        "tool_prompt_format": tool_prompt_format,
                        "tools": tools,
                    },
                    inference_chat_completion_params.InferenceChatCompletionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InferenceChatCompletionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def completion(
        self,
        *,
        content: inference_completion_params.Content,
        model: str,
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: inference_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceCompletionResponse:
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
        return cast(
            InferenceCompletionResponse,
            self._post(
                "/inference/completion",
                body=maybe_transform(
                    {
                        "content": content,
                        "model": model,
                        "logprobs": logprobs,
                        "response_format": response_format,
                        "sampling_params": sampling_params,
                        "stream": stream,
                    },
                    inference_completion_params.InferenceCompletionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InferenceCompletionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def embeddings(
        self,
        *,
        contents: List[inference_embeddings_params.Content],
        model: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingsResponse:
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
            "/inference/embeddings",
            body=maybe_transform(
                {
                    "contents": contents,
                    "model": model,
                },
                inference_embeddings_params.InferenceEmbeddingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingsResponse,
        )


class AsyncInferenceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncInferenceResourceWithStreamingResponse(self)

    async def chat_completion(
        self,
        *,
        messages: Iterable[inference_chat_completion_params.Message],
        model: str,
        logprobs: inference_chat_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: inference_chat_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        tool_choice: Literal["auto", "required"] | NotGiven = NOT_GIVEN,
        tool_prompt_format: Literal["json", "function_tag", "python_list"] | NotGiven = NOT_GIVEN,
        tools: Iterable[inference_chat_completion_params.Tool] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceChatCompletionResponse:
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
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return cast(
            InferenceChatCompletionResponse,
            await self._post(
                "/inference/chat_completion",
                body=await async_maybe_transform(
                    {
                        "messages": messages,
                        "model": model,
                        "logprobs": logprobs,
                        "response_format": response_format,
                        "sampling_params": sampling_params,
                        "stream": stream,
                        "tool_choice": tool_choice,
                        "tool_prompt_format": tool_prompt_format,
                        "tools": tools,
                    },
                    inference_chat_completion_params.InferenceChatCompletionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InferenceChatCompletionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def completion(
        self,
        *,
        content: inference_completion_params.Content,
        model: str,
        logprobs: inference_completion_params.Logprobs | NotGiven = NOT_GIVEN,
        response_format: inference_completion_params.ResponseFormat | NotGiven = NOT_GIVEN,
        sampling_params: SamplingParams | NotGiven = NOT_GIVEN,
        stream: bool | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InferenceCompletionResponse:
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
        return cast(
            InferenceCompletionResponse,
            await self._post(
                "/inference/completion",
                body=await async_maybe_transform(
                    {
                        "content": content,
                        "model": model,
                        "logprobs": logprobs,
                        "response_format": response_format,
                        "sampling_params": sampling_params,
                        "stream": stream,
                    },
                    inference_completion_params.InferenceCompletionParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, InferenceCompletionResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def embeddings(
        self,
        *,
        contents: List[inference_embeddings_params.Content],
        model: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EmbeddingsResponse:
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
            "/inference/embeddings",
            body=await async_maybe_transform(
                {
                    "contents": contents,
                    "model": model,
                },
                inference_embeddings_params.InferenceEmbeddingsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EmbeddingsResponse,
        )


class InferenceResourceWithRawResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.chat_completion = to_raw_response_wrapper(
            inference.chat_completion,
        )
        self.completion = to_raw_response_wrapper(
            inference.completion,
        )
        self.embeddings = to_raw_response_wrapper(
            inference.embeddings,
        )


class AsyncInferenceResourceWithRawResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.chat_completion = async_to_raw_response_wrapper(
            inference.chat_completion,
        )
        self.completion = async_to_raw_response_wrapper(
            inference.completion,
        )
        self.embeddings = async_to_raw_response_wrapper(
            inference.embeddings,
        )


class InferenceResourceWithStreamingResponse:
    def __init__(self, inference: InferenceResource) -> None:
        self._inference = inference

        self.chat_completion = to_streamed_response_wrapper(
            inference.chat_completion,
        )
        self.completion = to_streamed_response_wrapper(
            inference.completion,
        )
        self.embeddings = to_streamed_response_wrapper(
            inference.embeddings,
        )


class AsyncInferenceResourceWithStreamingResponse:
    def __init__(self, inference: AsyncInferenceResource) -> None:
        self._inference = inference

        self.chat_completion = async_to_streamed_response_wrapper(
            inference.chat_completion,
        )
        self.completion = async_to_streamed_response_wrapper(
            inference.completion,
        )
        self.embeddings = async_to_streamed_response_wrapper(
            inference.embeddings,
        )

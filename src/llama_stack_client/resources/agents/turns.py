# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
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
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.agents import turn_create_params, turn_retrieve_params
from ...types.agents.turn import Turn
from ...types.shared_params.attachment import Attachment
from ...types.agents.agents_turn_stream_chunk import AgentsTurnStreamChunk

__all__ = ["TurnsResource", "AsyncTurnsResource"]


class TurnsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TurnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return TurnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TurnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return TurnsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        session_id: str,
        attachments: Iterable[Attachment] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentsTurnStreamChunk:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        session_id: str,
        stream: Literal[True],
        attachments: Iterable[Attachment] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[AgentsTurnStreamChunk]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        session_id: str,
        stream: bool,
        attachments: Iterable[Attachment] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentsTurnStreamChunk | Stream[AgentsTurnStreamChunk]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "messages", "session_id"], ["agent_id", "messages", "session_id", "stream"])
    def create(
        self,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        session_id: str,
        attachments: Iterable[Attachment] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentsTurnStreamChunk | Stream[AgentsTurnStreamChunk]:
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return self._post(
            "/agents/turn/create",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "messages": messages,
                    "session_id": session_id,
                    "attachments": attachments,
                    "stream": stream,
                },
                turn_create_params.TurnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentsTurnStreamChunk,
            stream=stream or False,
            stream_cls=Stream[AgentsTurnStreamChunk],
        )

    def retrieve(
        self,
        *,
        agent_id: str,
        turn_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
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
            "/agents/turn/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agent_id": agent_id,
                        "turn_id": turn_id,
                    },
                    turn_retrieve_params.TurnRetrieveParams,
                ),
            ),
            cast_to=Turn,
        )


class AsyncTurnsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTurnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTurnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTurnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncTurnsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        session_id: str,
        attachments: Iterable[Attachment] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentsTurnStreamChunk:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        session_id: str,
        stream: Literal[True],
        attachments: Iterable[Attachment] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[AgentsTurnStreamChunk]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        session_id: str,
        stream: bool,
        attachments: Iterable[Attachment] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentsTurnStreamChunk | AsyncStream[AgentsTurnStreamChunk]:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "messages", "session_id"], ["agent_id", "messages", "session_id", "stream"])
    async def create(
        self,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        session_id: str,
        attachments: Iterable[Attachment] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentsTurnStreamChunk | AsyncStream[AgentsTurnStreamChunk]:
        extra_headers = {
            **strip_not_given({"X-LlamaStack-ProviderData": x_llama_stack_provider_data}),
            **(extra_headers or {}),
        }
        return await self._post(
            "/agents/turn/create",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "messages": messages,
                    "session_id": session_id,
                    "attachments": attachments,
                    "stream": stream,
                },
                turn_create_params.TurnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentsTurnStreamChunk,
            stream=stream or False,
            stream_cls=AsyncStream[AgentsTurnStreamChunk],
        )

    async def retrieve(
        self,
        *,
        agent_id: str,
        turn_id: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Turn:
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
            "/agents/turn/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "agent_id": agent_id,
                        "turn_id": turn_id,
                    },
                    turn_retrieve_params.TurnRetrieveParams,
                ),
            ),
            cast_to=Turn,
        )


class TurnsResourceWithRawResponse:
    def __init__(self, turns: TurnsResource) -> None:
        self._turns = turns

        self.create = to_raw_response_wrapper(
            turns.create,
        )
        self.retrieve = to_raw_response_wrapper(
            turns.retrieve,
        )


class AsyncTurnsResourceWithRawResponse:
    def __init__(self, turns: AsyncTurnsResource) -> None:
        self._turns = turns

        self.create = async_to_raw_response_wrapper(
            turns.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            turns.retrieve,
        )


class TurnsResourceWithStreamingResponse:
    def __init__(self, turns: TurnsResource) -> None:
        self._turns = turns

        self.create = to_streamed_response_wrapper(
            turns.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            turns.retrieve,
        )


class AsyncTurnsResourceWithStreamingResponse:
    def __init__(self, turns: AsyncTurnsResource) -> None:
        self._turns = turns

        self.create = async_to_streamed_response_wrapper(
            turns.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            turns.retrieve,
        )

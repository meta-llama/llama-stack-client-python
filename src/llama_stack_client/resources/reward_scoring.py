# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import reward_scoring_score_params
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
from ..types.reward_scoring_response import RewardScoringResponse

__all__ = ["RewardScoringResource", "AsyncRewardScoringResource"]


class RewardScoringResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RewardScoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return RewardScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RewardScoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return RewardScoringResourceWithStreamingResponse(self)

    def score(
        self,
        *,
        dialog_generations: Iterable[reward_scoring_score_params.DialogGeneration],
        model: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RewardScoringResponse:
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
            "/reward_scoring/score",
            body=maybe_transform(
                {
                    "dialog_generations": dialog_generations,
                    "model": model,
                },
                reward_scoring_score_params.RewardScoringScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardScoringResponse,
        )


class AsyncRewardScoringResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRewardScoringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRewardScoringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRewardScoringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncRewardScoringResourceWithStreamingResponse(self)

    async def score(
        self,
        *,
        dialog_generations: Iterable[reward_scoring_score_params.DialogGeneration],
        model: str,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RewardScoringResponse:
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
            "/reward_scoring/score",
            body=await async_maybe_transform(
                {
                    "dialog_generations": dialog_generations,
                    "model": model,
                },
                reward_scoring_score_params.RewardScoringScoreParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RewardScoringResponse,
        )


class RewardScoringResourceWithRawResponse:
    def __init__(self, reward_scoring: RewardScoringResource) -> None:
        self._reward_scoring = reward_scoring

        self.score = to_raw_response_wrapper(
            reward_scoring.score,
        )


class AsyncRewardScoringResourceWithRawResponse:
    def __init__(self, reward_scoring: AsyncRewardScoringResource) -> None:
        self._reward_scoring = reward_scoring

        self.score = async_to_raw_response_wrapper(
            reward_scoring.score,
        )


class RewardScoringResourceWithStreamingResponse:
    def __init__(self, reward_scoring: RewardScoringResource) -> None:
        self._reward_scoring = reward_scoring

        self.score = to_streamed_response_wrapper(
            reward_scoring.score,
        )


class AsyncRewardScoringResourceWithStreamingResponse:
    def __init__(self, reward_scoring: AsyncRewardScoringResource) -> None:
        self._reward_scoring = reward_scoring

        self.score = async_to_streamed_response_wrapper(
            reward_scoring.score,
        )

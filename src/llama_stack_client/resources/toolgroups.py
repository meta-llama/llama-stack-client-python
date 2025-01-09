# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ..types import (
    toolgroup_get_params,
    toolgroup_register_params,
    toolgroup_unregister_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.tool_group import ToolGroup
from ..types.mcp_config_param import McpConfigParam

__all__ = ["ToolgroupsResource", "AsyncToolgroupsResource"]


class ToolgroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolgroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return ToolgroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolgroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return ToolgroupsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolGroup:
        """
        List tool groups with optional provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/alpha/toolgroups/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGroup,
        )

    def get(
        self,
        *,
        toolgroup_id: str,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolGroup:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/alpha/toolgroups/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"toolgroup_id": toolgroup_id}, toolgroup_get_params.ToolgroupGetParams),
            ),
            cast_to=ToolGroup,
        )

    def register(
        self,
        *,
        provider_id: str,
        toolgroup_id: str,
        args: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        mcp_config: McpConfigParam | NotGiven = NOT_GIVEN,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Register a tool group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/alpha/toolgroups/register",
            body=maybe_transform(
                {
                    "provider_id": provider_id,
                    "toolgroup_id": toolgroup_id,
                    "args": args,
                    "mcp_config": mcp_config,
                },
                toolgroup_register_params.ToolgroupRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def unregister(
        self,
        *,
        tool_group_id: str,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Unregister a tool group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return self._post(
            "/alpha/toolgroups/unregister",
            body=maybe_transform(
                {"tool_group_id": tool_group_id}, toolgroup_unregister_params.ToolgroupUnregisterParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncToolgroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolgroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolgroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolgroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncToolgroupsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolGroup:
        """
        List tool groups with optional provider

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "application/jsonl", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/alpha/toolgroups/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolGroup,
        )

    async def get(
        self,
        *,
        toolgroup_id: str,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolGroup:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/alpha/toolgroups/get",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"toolgroup_id": toolgroup_id}, toolgroup_get_params.ToolgroupGetParams
                ),
            ),
            cast_to=ToolGroup,
        )

    async def register(
        self,
        *,
        provider_id: str,
        toolgroup_id: str,
        args: Dict[str, Union[bool, float, str, Iterable[object], object, None]] | NotGiven = NOT_GIVEN,
        mcp_config: McpConfigParam | NotGiven = NOT_GIVEN,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Register a tool group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/alpha/toolgroups/register",
            body=await async_maybe_transform(
                {
                    "provider_id": provider_id,
                    "toolgroup_id": toolgroup_id,
                    "args": args,
                    "mcp_config": mcp_config,
                },
                toolgroup_register_params.ToolgroupRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def unregister(
        self,
        *,
        tool_group_id: str,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Unregister a tool group

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {
            **strip_not_given(
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._post(
            "/alpha/toolgroups/unregister",
            body=await async_maybe_transform(
                {"tool_group_id": tool_group_id}, toolgroup_unregister_params.ToolgroupUnregisterParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ToolgroupsResourceWithRawResponse:
    def __init__(self, toolgroups: ToolgroupsResource) -> None:
        self._toolgroups = toolgroups

        self.list = to_raw_response_wrapper(
            toolgroups.list,
        )
        self.get = to_raw_response_wrapper(
            toolgroups.get,
        )
        self.register = to_raw_response_wrapper(
            toolgroups.register,
        )
        self.unregister = to_raw_response_wrapper(
            toolgroups.unregister,
        )


class AsyncToolgroupsResourceWithRawResponse:
    def __init__(self, toolgroups: AsyncToolgroupsResource) -> None:
        self._toolgroups = toolgroups

        self.list = async_to_raw_response_wrapper(
            toolgroups.list,
        )
        self.get = async_to_raw_response_wrapper(
            toolgroups.get,
        )
        self.register = async_to_raw_response_wrapper(
            toolgroups.register,
        )
        self.unregister = async_to_raw_response_wrapper(
            toolgroups.unregister,
        )


class ToolgroupsResourceWithStreamingResponse:
    def __init__(self, toolgroups: ToolgroupsResource) -> None:
        self._toolgroups = toolgroups

        self.list = to_streamed_response_wrapper(
            toolgroups.list,
        )
        self.get = to_streamed_response_wrapper(
            toolgroups.get,
        )
        self.register = to_streamed_response_wrapper(
            toolgroups.register,
        )
        self.unregister = to_streamed_response_wrapper(
            toolgroups.unregister,
        )


class AsyncToolgroupsResourceWithStreamingResponse:
    def __init__(self, toolgroups: AsyncToolgroupsResource) -> None:
        self._toolgroups = toolgroups

        self.list = async_to_streamed_response_wrapper(
            toolgroups.list,
        )
        self.get = async_to_streamed_response_wrapper(
            toolgroups.get,
        )
        self.register = async_to_streamed_response_wrapper(
            toolgroups.register,
        )
        self.unregister = async_to_streamed_response_wrapper(
            toolgroups.unregister,
        )

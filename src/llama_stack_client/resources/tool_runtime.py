# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable

import httpx

from ..types import tool_runtime_list_tools_params, tool_runtime_invoke_tool_params
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
from ..types.tool_def import ToolDef
from ..types.shared_params.url import URL
from ..types.tool_invocation_result import ToolInvocationResult

__all__ = ["ToolRuntimeResource", "AsyncToolRuntimeResource"]


class ToolRuntimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolRuntimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return ToolRuntimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolRuntimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return ToolRuntimeResourceWithStreamingResponse(self)

    def invoke_tool(
        self,
        *,
        args: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        tool_name: str,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolInvocationResult:
        """
        Run a tool with the given arguments

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
        return self._post(
            "/v1/tool-runtime/invoke",
            body=maybe_transform(
                {
                    "args": args,
                    "tool_name": tool_name,
                },
                tool_runtime_invoke_tool_params.ToolRuntimeInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolInvocationResult,
        )

    def list_tools(
        self,
        *,
        mcp_endpoint: URL | NotGiven = NOT_GIVEN,
        tool_group_id: str | NotGiven = NOT_GIVEN,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolDef:
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
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return self._get(
            "/v1/tool-runtime/list-tools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "mcp_endpoint": mcp_endpoint,
                        "tool_group_id": tool_group_id,
                    },
                    tool_runtime_list_tools_params.ToolRuntimeListToolsParams,
                ),
            ),
            cast_to=ToolDef,
        )


class AsyncToolRuntimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolRuntimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolRuntimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolRuntimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncToolRuntimeResourceWithStreamingResponse(self)

    async def invoke_tool(
        self,
        *,
        args: Dict[str, Union[bool, float, str, Iterable[object], object, None]],
        tool_name: str,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolInvocationResult:
        """
        Run a tool with the given arguments

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
        return await self._post(
            "/v1/tool-runtime/invoke",
            body=await async_maybe_transform(
                {
                    "args": args,
                    "tool_name": tool_name,
                },
                tool_runtime_invoke_tool_params.ToolRuntimeInvokeToolParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ToolInvocationResult,
        )

    async def list_tools(
        self,
        *,
        mcp_endpoint: URL | NotGiven = NOT_GIVEN,
        tool_group_id: str | NotGiven = NOT_GIVEN,
        x_llama_stack_client_version: str | NotGiven = NOT_GIVEN,
        x_llama_stack_provider_data: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ToolDef:
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
                {
                    "X-LlamaStack-Client-Version": x_llama_stack_client_version,
                    "X-LlamaStack-Provider-Data": x_llama_stack_provider_data,
                }
            ),
            **(extra_headers or {}),
        }
        return await self._get(
            "/v1/tool-runtime/list-tools",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "mcp_endpoint": mcp_endpoint,
                        "tool_group_id": tool_group_id,
                    },
                    tool_runtime_list_tools_params.ToolRuntimeListToolsParams,
                ),
            ),
            cast_to=ToolDef,
        )


class ToolRuntimeResourceWithRawResponse:
    def __init__(self, tool_runtime: ToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = to_raw_response_wrapper(
            tool_runtime.invoke_tool,
        )
        self.list_tools = to_raw_response_wrapper(
            tool_runtime.list_tools,
        )


class AsyncToolRuntimeResourceWithRawResponse:
    def __init__(self, tool_runtime: AsyncToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = async_to_raw_response_wrapper(
            tool_runtime.invoke_tool,
        )
        self.list_tools = async_to_raw_response_wrapper(
            tool_runtime.list_tools,
        )


class ToolRuntimeResourceWithStreamingResponse:
    def __init__(self, tool_runtime: ToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = to_streamed_response_wrapper(
            tool_runtime.invoke_tool,
        )
        self.list_tools = to_streamed_response_wrapper(
            tool_runtime.list_tools,
        )


class AsyncToolRuntimeResourceWithStreamingResponse:
    def __init__(self, tool_runtime: AsyncToolRuntimeResource) -> None:
        self._tool_runtime = tool_runtime

        self.invoke_tool = async_to_streamed_response_wrapper(
            tool_runtime.invoke_tool,
        )
        self.list_tools = async_to_streamed_response_wrapper(
            tool_runtime.list_tools,
        )

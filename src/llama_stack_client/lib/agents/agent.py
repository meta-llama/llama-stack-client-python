# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import asyncio
from typing import AsyncIterator, Iterator, List, Optional, Tuple, Union

from llama_stack_client import AsyncLlamaStackClient, LlamaStackClient

from llama_stack_client.types import ToolResponseMessage, UserMessage
from llama_stack_client.types.agent_create_params import AgentConfig
from llama_stack_client.types.agents.turn import CompletionMessage, Turn
from llama_stack_client.types.agents.turn_create_params import Document, Toolgroup
from llama_stack_client.types.agents.turn_create_response import AgentTurnResponseStreamChunk
from llama_stack_client.types.shared.tool_call import ToolCall

from .client_tool import ClientTool
from .tool_parser import ToolParser

DEFAULT_MAX_ITER = 10


class Agent:
    def __init__(
        self,
        client: Union[AsyncLlamaStackClient, LlamaStackClient],
        agent_config: AgentConfig,
        client_tools: Tuple[ClientTool] = (),
        tool_parser: Optional[ToolParser] = None,
    ):
        self.async_agent = AsyncAgent(client, agent_config, client_tools, tool_parser)
        asyncio.run(self.async_agent.initialize())
        self.sessions = self.async_agent.sessions
        self.client_tools = self.async_agent.client_tools
        self.tool_parser = self.async_agent.tool_parser
        self.builtin_tools = self.async_agent.builtin_tools
        self.agent_id = self.async_agent.agent_id

    def create_session(self, session_name: str) -> str:
        return asyncio.run(self.async_agent.create_session(session_name))

    def create_turn(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        stream: bool = True,
    ) -> Iterator[AgentTurnResponseStreamChunk] | Turn:
        if stream:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            def sync_generator():
                try:
                    async_stream = loop.run_until_complete(
                        self.async_agent.create_turn(messages, session_id, toolgroups, documents, stream)
                    )
                    while True:
                        chunk = loop.run_until_complete(async_stream.__anext__())
                        yield chunk
                except StopAsyncIteration:
                    pass
                finally:
                    loop.close()

            return sync_generator()
        else:
            return asyncio.run(self.async_agent.create_turn(messages, session_id, toolgroups, documents, stream))


class AsyncAgent:
    def __init__(
        self,
        client: Union[AsyncLlamaStackClient, LlamaStackClient],
        agent_config: AgentConfig,
        client_tools: Tuple[ClientTool] = (),
        tool_parser: Optional[ToolParser] = None,
    ):
        self.client = client
        self.agent_config = agent_config
        self.client_tools = {t.get_name(): t for t in client_tools}
        self.sessions = []
        self.tool_parser = tool_parser
        self.builtin_tools = {}

        self.is_async = True

        if isinstance(client, LlamaStackClient):
            self.is_async = False

    async def initialize(self) -> None:
        if self.is_async:
            agentic_system_create_response = await self.client.agents.create(
                agent_config=self.agent_config,
            )
        else:
            agentic_system_create_response = self.client.agents.create(
                agent_config=self.agent_config,
            )

        self.agent_id = agentic_system_create_response.agent_id
        for tg in self.agent_config["toolgroups"]:
            if self.is_async:
                for tool in await self.client.tools.list(toolgroup_id=tg):
                    self.builtin_tools[tool.identifier] = tool
            else:
                for tool in self.client.tools.list(toolgroup_id=tg):
                    self.builtin_tools[tool.identifier] = tool

    async def create_session(self, session_name: str) -> str:
        if self.is_async:
            agentic_system_create_session_response = await self.client.agents.session.create(
                agent_id=self.agent_id,
                session_name=session_name,
            )
        else:
            agentic_system_create_session_response = self.client.agents.session.create(
                agent_id=self.agent_id,
                session_name=session_name,
            )

        self.session_id = agentic_system_create_session_response.session_id
        self.sessions.append(self.session_id)
        return self.session_id

    async def create_turn(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
        stream: bool = True,
    ) -> AsyncIterator[AgentTurnResponseStreamChunk] | Turn:
        if stream:
            return self._create_turn_streaming(messages, session_id, toolgroups, documents)
        else:
            chunks = [x async for x in self._create_turn_streaming(messages, session_id, toolgroups, documents)]
            if not chunks:
                raise Exception("Turn did not complete")
            return chunks[-1].event.payload.turn

    async def _run_tool(self, tool_calls: List[ToolCall]) -> ToolResponseMessage:
        assert len(tool_calls) == 1, "Only one tool call is supported"
        tool_call = tool_calls[0]

        # custom client tools
        if tool_call.tool_name in self.client_tools:
            tool = self.client_tools[tool_call.tool_name]
            # NOTE: tool.run() expects a list of messages, we only pass in last message here
            # but we could pass in the entire message history
            messages = [
                CompletionMessage(
                    role="assistant",
                    content=tool_call.tool_name,
                    tool_calls=[tool_call],
                    stop_reason="end_of_turn",
                )
            ]
            if self.is_async:
                result_message = await tool.async_run(messages)
            else:
                result_message = tool.run(messages)

            return result_message

        # builtin tools executed by tool_runtime
        if tool_call.tool_name in self.builtin_tools:
            if self.is_async:
                tool_result = await self.client.tool_runtime.invoke_tool(
                    tool_name=tool_call.tool_name,
                    kwargs=tool_call.arguments,
                )
            else:
                tool_result = self.client.tool_runtime.invoke_tool(
                    tool_name=tool_call.tool_name,
                    kwargs=tool_call.arguments,
                )
            tool_response_message = ToolResponseMessage(
                call_id=tool_call.call_id,
                tool_name=tool_call.tool_name,
                content=tool_result.content,
                role="tool",
            )
            return tool_response_message

        # cannot find tools
        return ToolResponseMessage(
            call_id=tool_call.call_id,
            tool_name=tool_call.tool_name,
            content=f"Unknown tool `{tool_call.tool_name}` was called.",
            role="tool",
        )

    async def _create_turn_streaming(
        self,
        messages: List[Union[UserMessage, ToolResponseMessage]],
        session_id: Optional[str] = None,
        toolgroups: Optional[List[Toolgroup]] = None,
        documents: Optional[List[Document]] = None,
    ) -> AsyncIterator[AgentTurnResponseStreamChunk]:
        n_iter = 0
        max_iter = self.agent_config.get("max_infer_iters", DEFAULT_MAX_ITER)

        # 1. create an agent turn
        if self.is_async:
            turn_response = await self.client.agents.turn.create(
                agent_id=self.agent_id,
                # use specified session_id or last session created
                session_id=session_id or self.session_id[-1],
                messages=messages,
                stream=True,
                documents=documents,
                toolgroups=toolgroups,
                allow_turn_resume=True,
            )
        else:
            turn_response = self.client.agents.turn.create(
                agent_id=self.agent_id,
                # use specified session_id or last session created
                session_id=session_id or self.session_id[-1],
                messages=messages,
                stream=True,
                documents=documents,
                toolgroups=toolgroups,
                allow_turn_resume=True,
            )

        # 2. process turn and resume if there's a tool call
        is_turn_complete = False
        while not is_turn_complete:
            is_turn_complete = True

            if self.is_async:
                async for chunk in turn_response:
                    tool_calls = self._get_tool_calls(chunk)
                    if hasattr(chunk, "error"):
                        yield chunk
                        return
                    elif not tool_calls:
                        yield chunk
                    else:
                        is_turn_complete = False
                        turn_id = self._get_turn_id(chunk)
                        if n_iter == 0:
                            yield chunk

                        # run the tools
                        tool_response_message = await self._run_tool(tool_calls)

                        # pass it to next iteration
                        turn_response = await self.client.agents.turn.resume(
                            agent_id=self.agent_id,
                            session_id=session_id or self.session_id[-1],
                            turn_id=turn_id,
                            tool_responses=[tool_response_message],
                            stream=True,
                        )

                        n_iter += 1
            else:
                for chunk in turn_response:
                    tool_calls = self._get_tool_calls(chunk)
                    if hasattr(chunk, "error"):
                        yield chunk
                        return
                    elif not tool_calls:
                        yield chunk
                    else:
                        is_turn_complete = False
                        turn_id = self._get_turn_id(chunk)
                        if n_iter == 0:
                            yield chunk

                        # run the tools
                        tool_response_message = await self._run_tool(tool_calls)

                        # pass it to next iteration
                        turn_response = self.client.agents.turn.resume(
                            agent_id=self.agent_id,
                            session_id=session_id or self.session_id[-1],
                            turn_id=turn_id,
                            tool_responses=[tool_response_message],
                            stream=True,
                        )

                        n_iter += 1

            if n_iter >= max_iter:
                raise Exception(f"Turn did not complete in {max_iter} iterations")

    def _get_tool_calls(self, chunk: AgentTurnResponseStreamChunk) -> List[ToolCall]:
        if chunk.event.payload.event_type not in {"turn_complete", "turn_awaiting_input"}:
            return []

        message = chunk.event.payload.turn.output_message
        if message.stop_reason == "out_of_tokens":
            return []

        if self.tool_parser:
            return self.tool_parser.get_tool_calls(message)

        return message.tool_calls

    def _get_turn_id(self, chunk: AgentTurnResponseStreamChunk) -> Optional[str]:
        if chunk.event.payload.event_type not in ["turn_complete", "turn_awaiting_input"]:
            return None

        return chunk.event.payload.turn.turn_id

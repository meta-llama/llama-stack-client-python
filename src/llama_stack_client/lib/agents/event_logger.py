# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import List, Optional, Union

from termcolor import cprint

from llama_stack_client.types import ToolResponseMessage


def interleaved_text_media_as_str(
    content: Union[str, List[str]], sep: str = " "
) -> str:
    def _process(c) -> str:
        if isinstance(c, str):
            return c
        else:
            return "<media>"

    if isinstance(content, list):
        return sep.join(_process(c) for c in content)
    else:
        return _process(content)


class LogEvent:
    def __init__(
        self,
        role: Optional[str] = None,
        content: str = "",
        end: str = "\n",
        color="white",
    ):
        self.role = role
        self.content = content
        self.color = color
        self.end = "\n" if end is None else end

    def __str__(self):
        if self.role is not None:
            return f"{self.role}> {self.content}"
        else:
            return f"{self.content}"

    def print(self, flush=True):
        cprint(f"{str(self)}", color=self.color, end=self.end, flush=flush)


class EventLogger:
    def _get_log_event(self, chunk, previous_event_type=None, previous_step_type=None):
        if hasattr(chunk, "error"):
            yield LogEvent(role=None, content=chunk.error["message"], color="red")
            return

        if not hasattr(chunk, "event"):
            # Need to check for custom tool first
            # since it does not produce event but instead
            # a Message
            if isinstance(chunk, ToolResponseMessage):
                yield LogEvent(role="CustomTool", content=chunk.content, color="green")
                return

        event = chunk.event
        event_type = event.payload.event_type

        if event_type in {"turn_start", "turn_complete"}:
            # Currently not logging any turn realted info
            yield LogEvent(role=None, content="", end="", color="grey")
            return

        step_type = event.payload.step_type
        # handle safety
        if step_type == "shield_call" and event_type == "step_complete":
            violation = event.payload.step_details.violation
            if not violation:
                yield LogEvent(role=step_type, content="No Violation", color="magenta")
            else:
                yield LogEvent(
                    role=step_type,
                    content=f"{violation.metadata} {violation.user_message}",
                    color="red",
                )

        # handle inference
        if step_type == "inference":
            if event_type == "step_start":
                yield LogEvent(role=step_type, content="", end="", color="yellow")
            elif event_type == "step_progress":
                if event.payload.tool_call_delta:
                    if isinstance(event.payload.tool_call_delta.content, str):
                        yield LogEvent(
                            role=None,
                            content=event.payload.tool_call_delta.content,
                            end="",
                            color="cyan",
                        )
                else:
                    yield LogEvent(
                        role=None,
                        content=event.payload.text_delta,
                        end="",
                        color="yellow",
                    )
            else:
                # step complete
                yield LogEvent(role=None, content="")

        # handle tool_execution
        if step_type == "tool_execution" and event_type == "step_complete":
            # Only print tool calls and responses at the step_complete event
            details = event.payload.step_details
            for t in details.tool_calls:
                yield LogEvent(
                    role=step_type,
                    content=f"Tool:{t.tool_name} Args:{t.arguments}",
                    color="green",
                )

            for r in details.tool_responses:
                yield LogEvent(
                    role=step_type,
                    content=f"Tool:{r.tool_name} Response:{r.content}",
                    color="green",
                )

        # memory retrieval
        if step_type == "memory_retrieval" and event_type == "step_complete":
            details = event.payload.step_details
            content = interleaved_text_media_as_str(details.inserted_context)
            content = content[:200] + "..." if len(content) > 200 else content

            yield LogEvent(
                role=step_type,
                content=f"Retrieved context from banks: {details.memory_bank_ids}.\n====\n{content}\n>",
                color="cyan",
            )

    def _get_event_type_step_type(self, chunk):
        if hasattr(chunk, "event"):
            previous_event_type = (
                chunk.event.payload.event_type if hasattr(chunk, "event") else None
            )
            previous_step_type = (
                chunk.event.payload.step_type
                if previous_event_type not in {"turn_start", "turn_complete"}
                else None
            )
            return previous_event_type, previous_step_type
        return None, None

    def log(self, event_generator):
        previous_event_type = None
        previous_step_type = None

        for chunk in event_generator:
            for log_event in self._get_log_event(
                chunk, previous_event_type, previous_step_type
            ):
                yield log_event
            previous_event_type, previous_step_type = self._get_event_type_step_type(
                chunk
            )

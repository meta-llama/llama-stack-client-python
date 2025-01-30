# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

from termcolor import cprint

from llama_stack_client.types import InterleavedContent, ToolResponseMessage


def interleaved_content_as_str(content: InterleavedContent, sep: str = " ") -> str:
    def _process(c) -> str:
        if isinstance(c, str):
            return c
        elif hasattr(c, "type"):
            if c.type == "text":
                return c.text
            elif c.type == "image":
                return "<image>"
            else:
                raise ValueError(f"Unexpected type {c}")
        else:
            raise ValueError(f"Unsupported content type: {type(c)}")

    if isinstance(content, list):
        return sep.join(_process(c) for c in content)
    else:
        return _process(content)


class TurnStreamLogEvent:
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


class TurnStreamEventLogger:
    def __init__(self):
        self.previous_event_type = None
        self.previous_step_type = None

    def process_chunk(self, chunk):
        log_event = self._get_log_event(
            chunk, self.previous_event_type, self.previous_step_type
        )
        self.previous_event_type, self.previous_step_type = (
            self._get_event_type_step_type(chunk)
        )
        return log_event

    def _get_log_event(self, chunk, previous_event_type=None, previous_step_type=None):
        if hasattr(chunk, "error"):
            yield TurnStreamLogEvent(
                role=None, content=chunk.error["message"], color="red"
            )
            return

        if not hasattr(chunk, "event"):
            # Need to check for custom tool first
            # since it does not produce event but instead
            # a Message
            if isinstance(chunk, ToolResponseMessage):
                yield TurnStreamLogEvent(
                    role="CustomTool", content=chunk.content, color="green"
                )
                return

        event = chunk.event
        event_type = event.payload.event_type

        if event_type in {"turn_start", "turn_complete"}:
            # Currently not logging any turn realted info
            yield TurnStreamLogEvent(role=None, content="", end="", color="grey")
            return

        step_type = event.payload.step_type
        # handle safety
        if step_type == "shield_call" and event_type == "step_complete":
            violation = event.payload.step_details.violation
            if not violation:
                yield TurnStreamLogEvent(
                    role=step_type, content="No Violation", color="magenta"
                )
            else:
                yield TurnStreamLogEvent(
                    role=step_type,
                    content=f"{violation.metadata} {violation.user_message}",
                    color="red",
                )

        # handle inference
        if step_type == "inference":
            if event_type == "step_start":
                yield TurnStreamLogEvent(
                    role=step_type, content="", end="", color="yellow"
                )
            elif event_type == "step_progress":
                if event.payload.delta.type == "tool_call":
                    if isinstance(event.payload.delta.tool_call, str):
                        yield TurnStreamLogEvent(
                            role=None,
                            content=event.payload.delta.tool_call,
                            end="",
                            color="cyan",
                        )
                elif event.payload.delta.type == "text":
                    yield TurnStreamLogEvent(
                        role=None,
                        content=event.payload.delta.text,
                        end="",
                        color="yellow",
                    )
            else:
                # step complete
                yield TurnStreamLogEvent(role=None, content="")

        # handle tool_execution
        if step_type == "tool_execution" and event_type == "step_complete":
            # Only print tool calls and responses at the step_complete event
            details = event.payload.step_details
            for t in details.tool_calls:
                yield TurnStreamLogEvent(
                    role=step_type,
                    content=f"Tool:{t.tool_name} Args:{t.arguments}",
                    color="green",
                )

            for r in details.tool_responses:
                if r.tool_name == "query_from_memory":
                    inserted_context = interleaved_content_as_str(r.content)
                    content = f"fetched {len(inserted_context)} bytes from memory"

                    yield TurnStreamLogEvent(
                        role=step_type,
                        content=content,
                        color="cyan",
                    )
                else:
                    yield TurnStreamLogEvent(
                        role=step_type,
                        content=f"Tool:{r.tool_name} Response:{r.content}",
                        color="green",
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


class EventLogger:
    def log(self, event_generator):
        logger = TurnStreamEventLogger()
        for chunk in event_generator:
            log_event = logger.process_chunk(chunk)
            if log_event:
                yield log_event

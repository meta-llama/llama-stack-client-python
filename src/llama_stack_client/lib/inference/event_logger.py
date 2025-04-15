# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from termcolor import cprint


class InferenceStreamPrintableEvent:
    def __init__(
        self,
        content: str = "",
        end: str = "\n",
        color="white",
    ):
        self.content = content
        self.color = color
        self.end = "\n" if end is None else end

    def print(self, flush=True):
        cprint(f"{self.content}", color=self.color, end=self.end, flush=flush)


class InferenceStreamLogEventPrinter:
    def __init__(self):
        self.is_thinking = False

    def yield_printable_events(self, chunk):
        event = chunk.event
        if event.event_type == "start":
            yield InferenceStreamPrintableEvent("Assistant> ", color="cyan", end="")
        elif event.event_type == "progress":
            if event.delta.type == "reasoning":
                if not self.is_thinking:
                    yield InferenceStreamPrintableEvent("<thinking> ", color="magenta", end="")
                    self.is_thinking = True
                yield InferenceStreamPrintableEvent(event.delta.reasoning, color="magenta", end="")
            else:
                if self.is_thinking:
                    yield InferenceStreamPrintableEvent("</thinking>", color="magenta", end="")
                    self.is_thinking = False
                yield InferenceStreamPrintableEvent(event.delta.text, color="yellow", end="")
        elif event.event_type == "complete":
            yield InferenceStreamPrintableEvent("")


class EventLogger:
    def log(self, event_generator):
        printer = InferenceStreamLogEventPrinter()
        for chunk in event_generator:
            yield from printer.yield_printable_events(chunk)

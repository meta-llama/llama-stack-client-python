# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from termcolor import cprint


class LogEvent:
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


class EventLogger:
    def log(self, event_generator):
        for chunk in event_generator:
            event = chunk.event
            # TODO: discrepancy between DirectClient & HTTP Client
            event_type = event.event_type if type(event.event_type) == str else event.event_type.value                
            if event_type == "start":
                yield LogEvent("Assistant> ", color="cyan", end="")
            elif event_type == "progress":
                yield LogEvent(event.delta, color="yellow", end="")
            elif event_type == "complete":
                yield LogEvent("")

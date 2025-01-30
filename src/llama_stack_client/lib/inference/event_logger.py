# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
from termcolor import cprint


class InferenceStreamLogEvent:
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


class InferenceStreamLogEventLogger:
    def process_chunk(self, chunk):
        event = chunk.event
        if event.event_type == "start":
            return InferenceStreamLogEvent("Assistant> ", color="cyan", end="")
        elif event.event_type == "progress":
            return InferenceStreamLogEvent(event.delta.text, color="yellow", end="")
        elif event.event_type == "complete":
            return InferenceStreamLogEvent("")
        return None


class EventLogger:
    def log(self, event_generator):
        logger = InferenceStreamLogEventLogger()
        for chunk in event_generator:
            log_event = logger.process_chunk(chunk)
            if log_event:
                yield log_event

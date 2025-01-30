from .agents.event_logger import TurnStreamEventPrinter
from .inference.event_logger import InferenceStreamLogEventPrinter


class EventStreamPrinter:
    @classmethod
    def gen(cls, event_generator):
        inference_printer = None
        turn_printer = None
        for chunk in event_generator:
            if not hasattr(chunk, "event"):
                raise ValueError(f"Unexpected chunk without event: {chunk}")

            event = chunk.event
            if hasattr(event, "event_type"):
                if not inference_printer:
                    inference_printer = InferenceStreamLogEventPrinter()
                printable_event = inference_printer.process_chunk(chunk)
                if printable_event:
                    yield printable_event
            elif hasattr(event, "payload") and hasattr(event.payload, "event_type"):
                if not turn_printer:
                    turn_printer = TurnStreamEventPrinter()
                printable_event = turn_printer.process_chunk(chunk)
                if printable_event:
                    yield printable_event
            else:
                raise ValueError(f"Unsupported event: {event}")

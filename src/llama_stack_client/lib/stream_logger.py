from .agents.event_logger import TurnStreamEventLogger
from .inference.event_logger import InferenceStreamLogEventLogger


class EventLogger:
    def log(self, event_generator):
        inference_logger = None
        turn_logger = None
        for chunk in event_generator:
            if not hasattr(chunk, "event"):
                raise ValueError(f"Unexpected chunk without event: {chunk}")

            event = chunk.event
            if hasattr(event, "event_type"):
                if not inference_logger:
                    inference_logger = InferenceStreamLogEventLogger()
                log_event = inference_logger.process_chunk(chunk)
                if log_event:
                    yield log_event
            elif hasattr(event, "payload") and hasattr(event.payload, "event_type"):
                if not turn_logger:
                    turn_logger = TurnStreamEventLogger()
                log_event = turn_logger.process_chunk(chunk)
                if log_event:
                    yield log_event
            else:
                raise ValueError(f"Unsupported event: {event}")

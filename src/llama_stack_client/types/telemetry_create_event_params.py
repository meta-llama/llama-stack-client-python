# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .event_type import EventType
from .structured_log_type import StructuredLogType

__all__ = [
    "TelemetryCreateEventParams",
    "Event",
    "EventUnstructuredLogEvent",
    "EventMetricEvent",
    "EventStructuredLogEvent",
    "EventStructuredLogEventPayload",
    "EventStructuredLogEventPayloadSpanStartPayload",
    "EventStructuredLogEventPayloadSpanEndPayload",
]


class TelemetryCreateEventParams(TypedDict, total=False):
    event: Required[Event]

    ttl_seconds: Required[int]


class EventUnstructuredLogEvent(TypedDict, total=False):
    message: Required[str]

    severity: Required[Literal["verbose", "debug", "info", "warn", "error", "critical"]]

    span_id: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    trace_id: Required[str]

    type: Required[EventType]

    attributes: Dict[str, Union[str, float, bool, None]]


class EventMetricEvent(TypedDict, total=False):
    metric: Required[str]

    span_id: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    trace_id: Required[str]

    type: Required[EventType]

    unit: Required[str]

    value: Required[float]

    attributes: Dict[str, Union[str, float, bool, None]]


class EventStructuredLogEventPayloadSpanStartPayload(TypedDict, total=False):
    name: Required[str]

    type: Required[StructuredLogType]

    parent_span_id: str


class EventStructuredLogEventPayloadSpanEndPayload(TypedDict, total=False):
    status: Required[Literal["ok", "error"]]

    type: Required[StructuredLogType]


EventStructuredLogEventPayload: TypeAlias = Union[
    EventStructuredLogEventPayloadSpanStartPayload, EventStructuredLogEventPayloadSpanEndPayload
]


class EventStructuredLogEvent(TypedDict, total=False):
    payload: Required[EventStructuredLogEventPayload]

    span_id: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    trace_id: Required[str]

    type: Required[EventType]

    attributes: Dict[str, Union[str, float, bool, None]]


Event: TypeAlias = Union[EventUnstructuredLogEvent, EventMetricEvent, EventStructuredLogEvent]

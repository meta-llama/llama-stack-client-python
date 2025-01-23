# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TelemetryLogEventParams",
    "Event",
    "EventUnstructuredLog",
    "EventMetric",
    "EventStructuredLog",
    "EventStructuredLogPayload",
    "EventStructuredLogPayloadSpanStart",
    "EventStructuredLogPayloadSpanEnd",
]


class TelemetryLogEventParams(TypedDict, total=False):
    event: Required[Event]

    ttl_seconds: Required[int]

    x_llama_stack_client_version: Annotated[str, PropertyInfo(alias="X-LlamaStack-Client-Version")]

    x_llama_stack_provider_data: Annotated[str, PropertyInfo(alias="X-LlamaStack-Provider-Data")]


class EventUnstructuredLog(TypedDict, total=False):
    message: Required[str]

    severity: Required[Literal["verbose", "debug", "info", "warn", "error", "critical"]]

    span_id: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    trace_id: Required[str]

    type: Required[Literal["unstructured_log"]]

    attributes: Dict[str, Union[bool, float, str, Iterable[object], object, None]]


class EventMetric(TypedDict, total=False):
    metric: Required[str]

    span_id: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    trace_id: Required[str]

    type: Required[Literal["metric"]]

    unit: Required[str]

    value: Required[float]

    attributes: Dict[str, Union[bool, float, str, Iterable[object], object, None]]


class EventStructuredLogPayloadSpanStart(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["span_start"]]

    parent_span_id: str


class EventStructuredLogPayloadSpanEnd(TypedDict, total=False):
    status: Required[Literal["ok", "error"]]

    type: Required[Literal["span_end"]]


EventStructuredLogPayload: TypeAlias = Union[EventStructuredLogPayloadSpanStart, EventStructuredLogPayloadSpanEnd]


class EventStructuredLog(TypedDict, total=False):
    payload: Required[EventStructuredLogPayload]

    span_id: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    trace_id: Required[str]

    type: Required[Literal["structured_log"]]

    attributes: Dict[str, Union[bool, float, str, Iterable[object], object, None]]


Event: TypeAlias = Union[EventUnstructuredLog, EventMetric, EventStructuredLog]

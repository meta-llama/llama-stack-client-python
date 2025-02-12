# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EventParam",
    "UnstructuredLogEvent",
    "MetricEvent",
    "StructuredLogEvent",
    "StructuredLogEventPayload",
    "StructuredLogEventPayloadSpanStartPayload",
    "StructuredLogEventPayloadSpanEndPayload",
]


class UnstructuredLogEvent(TypedDict, total=False):
    message: Required[str]

    severity: Required[Literal["verbose", "debug", "info", "warn", "error", "critical"]]

    span_id: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    trace_id: Required[str]

    type: Required[Literal["unstructured_log"]]

    attributes: Dict[str, Union[str, float, bool, None]]


class MetricEvent(TypedDict, total=False):
    metric: Required[str]

    span_id: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    trace_id: Required[str]

    type: Required[Literal["metric"]]

    unit: Required[str]

    value: Required[float]

    attributes: Dict[str, Union[str, float, bool, None]]


class StructuredLogEventPayloadSpanStartPayload(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["span_start"]]

    parent_span_id: str


class StructuredLogEventPayloadSpanEndPayload(TypedDict, total=False):
    status: Required[Literal["ok", "error"]]

    type: Required[Literal["span_end"]]


StructuredLogEventPayload: TypeAlias = Union[
    StructuredLogEventPayloadSpanStartPayload, StructuredLogEventPayloadSpanEndPayload
]


class StructuredLogEvent(TypedDict, total=False):
    payload: Required[StructuredLogEventPayload]

    span_id: Required[str]

    timestamp: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]

    trace_id: Required[str]

    type: Required[Literal["structured_log"]]

    attributes: Dict[str, Union[str, float, bool, None]]


EventParam: TypeAlias = Union[UnstructuredLogEvent, MetricEvent, StructuredLogEvent]

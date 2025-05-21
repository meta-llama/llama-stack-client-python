# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .event_param import EventParam

__all__ = ["TelemetryLogEventParams"]


class TelemetryLogEventParams(TypedDict, total=False):
    event: Required[EventParam]
    """The event to log."""

    ttl_seconds: Required[int]
    """The time to live of the event."""

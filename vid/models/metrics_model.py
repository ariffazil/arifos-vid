"""Metrics model for the VID pipeline.

This module defines Pydantic models for metrics and telemetry data.
"""

from pydantic import BaseModel


class MetricsModel(BaseModel):
    """Model representing pipeline metrics.

    Attributes:
        name: Name of the metric.
        value: Value of the metric.
        unit: Unit of measurement.
    """

    name: str | None = None
    value: float | None = None
    unit: str | None = None


class TelemetryData(BaseModel):
    """Model representing telemetry data.

    Attributes:
        timestamp: Timestamp of the telemetry event.
        source: Source of the telemetry.
        metrics: List of metrics collected.
    """

    timestamp: str | None = None
    source: str | None = None
    metrics: list[MetricsModel] | None = None

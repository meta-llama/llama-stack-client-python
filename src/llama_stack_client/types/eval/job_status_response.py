# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["JobStatusResponse"]

JobStatusResponse: TypeAlias = Literal["completed", "in_progress", "failed", "scheduled"]

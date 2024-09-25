# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["TrainEvalDatasetParam"]


class TrainEvalDatasetParam(TypedDict, total=False):
    columns: Required[Dict[str, Literal["dialog", "text", "media", "number", "json"]]]

    content_url: Required[str]

    metadata: Dict[str, Union[bool, float, str, Iterable[object], object, None]]

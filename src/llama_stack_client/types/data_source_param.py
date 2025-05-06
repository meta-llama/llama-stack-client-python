# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["DataSourceParam", "UriDataSource", "RowsDataSource"]


class UriDataSource(TypedDict, total=False):
    type: Required[Literal["uri"]]

    uri: Required[str]
    """The dataset can be obtained from a URI.

    E.g. - "https://mywebsite.com/mydata.jsonl" - "lsfs://mydata.jsonl" -
    "data:csv;base64,{base64_content}"
    """


class RowsDataSource(TypedDict, total=False):
    rows: Required[Iterable[Dict[str, Union[bool, float, str, Iterable[object], object, None]]]]
    """The dataset is stored in rows.

    E.g. - [ {"messages": [{"role": "user", "content": "Hello, world!"}, {"role":
    "assistant", "content": "Hello, world!"}]} ]
    """

    type: Required[Literal["rows"]]


DataSourceParam: TypeAlias = Union[UriDataSource, RowsDataSource]

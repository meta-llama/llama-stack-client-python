# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["DataSource", "UriDataSource", "RowsDataSource"]


class UriDataSource(BaseModel):
    type: Literal["uri"]

    uri: str
    """The dataset can be obtained from a URI.

    E.g. - "https://mywebsite.com/mydata.jsonl" - "lsfs://mydata.jsonl" -
    "data:csv;base64,{base64_content}"
    """


class RowsDataSource(BaseModel):
    rows: List[Dict[str, Union[bool, float, str, List[object], object, None]]]
    """The dataset is stored in rows.

    E.g. - [ {"messages": [{"role": "user", "content": "Hello, world!"}, {"role":
    "assistant", "content": "Hello, world!"}]} ]
    """

    type: Literal["rows"]


DataSource: TypeAlias = Annotated[Union[UriDataSource, RowsDataSource], PropertyInfo(discriminator="type")]

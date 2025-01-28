# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["ResponseFormat", "JsonSchemaResponseFormat", "GrammarResponseFormat"]


class JsonSchemaResponseFormat(BaseModel):
    json_schema: Dict[str, Union[bool, float, str, List[object], object, None]]

    type: Literal["json_schema"]


class GrammarResponseFormat(BaseModel):
    bnf: Dict[str, Union[bool, float, str, List[object], object, None]]

    type: Literal["grammar"]


ResponseFormat: TypeAlias = Annotated[
    Union[JsonSchemaResponseFormat, GrammarResponseFormat], PropertyInfo(discriminator="type")
]

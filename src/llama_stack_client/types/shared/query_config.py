# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["QueryConfig", "QueryGeneratorConfig", "QueryGeneratorConfigDefault", "QueryGeneratorConfigLlm"]


class QueryGeneratorConfigDefault(BaseModel):
    separator: str

    type: Literal["default"]


class QueryGeneratorConfigLlm(BaseModel):
    model: str

    template: str

    type: Literal["llm"]


QueryGeneratorConfig: TypeAlias = Annotated[
    Union[QueryGeneratorConfigDefault, QueryGeneratorConfigLlm], PropertyInfo(discriminator="type")
]


class QueryConfig(BaseModel):
    max_chunks: int

    max_tokens_in_context: int

    query_generator_config: QueryGeneratorConfig

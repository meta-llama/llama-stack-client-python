# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel
from .query_generator_config import QueryGeneratorConfig

__all__ = ["QueryConfig"]


class QueryConfig(BaseModel):
    max_chunks: int

    max_tokens_in_context: int

    query_generator_config: QueryGeneratorConfig

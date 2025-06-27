# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["QueryGeneratorConfig", "DefaultRagQueryGeneratorConfig", "LlmragQueryGeneratorConfig"]


class DefaultRagQueryGeneratorConfig(BaseModel):
    separator: str

    type: Literal["default"]


class LlmragQueryGeneratorConfig(BaseModel):
    model: str

    template: str

    type: Literal["llm"]


QueryGeneratorConfig: TypeAlias = Annotated[
    Union[DefaultRagQueryGeneratorConfig, LlmragQueryGeneratorConfig], PropertyInfo(discriminator="type")
]

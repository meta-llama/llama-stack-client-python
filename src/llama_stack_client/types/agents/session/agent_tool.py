# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["AgentTool", "AgentToolGroupWithArgs"]


class AgentToolGroupWithArgs(BaseModel):
    args: Dict[str, Union[bool, float, str, List[object], object, None]]

    name: str


AgentTool: TypeAlias = Union[str, AgentToolGroupWithArgs]

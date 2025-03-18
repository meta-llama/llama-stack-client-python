# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolCall"]


class ToolCall(BaseModel):
    arguments: Union[
        str,
        Dict[
            str,
            Union[
                str, float, bool, List[Union[str, float, bool, None]], Dict[str, Union[str, float, bool, None]], None
            ],
        ],
    ]

    call_id: str

    tool_name: Union[Literal["brave_search", "wolfram_alpha", "photogen", "code_interpreter"], str]

    arguments_json: Optional[str] = None

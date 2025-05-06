# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .tool_def import ToolDef
from .tool_config import ToolConfig
from .response_format import ResponseFormat
from .sampling_params import SamplingParams
from .agents.session.agent_tool import AgentTool

__all__ = ["AgentConfig"]


class AgentConfig(BaseModel):
    instructions: str
    """The system instructions for the agent"""

    model: str
    """The model identifier to use for the agent"""

    client_tools: Optional[List[ToolDef]] = None

    enable_session_persistence: Optional[bool] = None
    """Optional flag indicating whether session data has to be persisted"""

    input_shields: Optional[List[str]] = None

    max_infer_iters: Optional[int] = None

    name: Optional[str] = None
    """Optional name for the agent, used in telemetry and identification"""

    output_shields: Optional[List[str]] = None

    response_format: Optional[ResponseFormat] = None
    """Optional response format configuration"""

    sampling_params: Optional[SamplingParams] = None
    """Sampling parameters."""

    tool_choice: Optional[Literal["auto", "required", "none"]] = None
    """Whether tool use is required or automatic.

    This is a hint to the model which may not be followed. It depends on the
    Instruction Following capabilities of the model.
    """

    tool_config: Optional[ToolConfig] = None
    """Configuration for tool use."""

    tool_prompt_format: Optional[Literal["json", "function_tag", "python_list"]] = None
    """Prompt format for calling custom / zero shot tools."""

    toolgroups: Optional[List[AgentTool]] = None

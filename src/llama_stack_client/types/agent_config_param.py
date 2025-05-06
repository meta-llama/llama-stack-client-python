# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .tool_def_param import ToolDefParam
from .tool_config_param import ToolConfigParam
from .response_format_param import ResponseFormatParam
from .sampling_params_param import SamplingParamsParam
from .agents.session.agent_tool_param import AgentToolParam

__all__ = ["AgentConfigParam"]


class AgentConfigParam(TypedDict, total=False):
    instructions: Required[str]
    """The system instructions for the agent"""

    model: Required[str]
    """The model identifier to use for the agent"""

    client_tools: Iterable[ToolDefParam]

    enable_session_persistence: bool
    """Optional flag indicating whether session data has to be persisted"""

    input_shields: List[str]

    max_infer_iters: int

    name: str
    """Optional name for the agent, used in telemetry and identification"""

    output_shields: List[str]

    response_format: ResponseFormatParam
    """Optional response format configuration"""

    sampling_params: SamplingParamsParam
    """Sampling parameters."""

    tool_choice: Literal["auto", "required", "none"]
    """Whether tool use is required or automatic.

    This is a hint to the model which may not be followed. It depends on the
    Instruction Following capabilities of the model.
    """

    tool_config: ToolConfigParam
    """Configuration for tool use."""

    tool_prompt_format: Literal["json", "function_tag", "python_list"]
    """Prompt format for calling custom / zero shot tools."""

    toolgroups: List[AgentToolParam]

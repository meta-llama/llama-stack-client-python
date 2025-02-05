# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from pydantic import BaseModel, ValidationError
from typing import Dict, Any, Optional
from ..output_parser import OutputParser
from llama_stack_client.types.shared.completion_message import CompletionMessage
from llama_stack_client.types.shared.tool_call import ToolCall

import uuid


class Action(BaseModel):
    tool_name: str
    tool_params: Dict[str, Any]


class ReActOutput(BaseModel):
    thought: str
    action: Optional[Action] = None
    answer: Optional[str] = None


class ReActOutputParser(OutputParser):
    def parse(self, output_message: CompletionMessage) -> None:
        response_text = str(output_message.content)
        try:
            react_output = ReActOutput.model_validate_json(response_text)
        except ValidationError as e:
            print(f"Error parsing action: {e}")
            return 

        if react_output.answer:
            return 

        if react_output.action:
            tool_name = react_output.action.tool_name
            tool_params = react_output.action.tool_params
            if tool_name and tool_params:
                call_id = str(uuid.uuid4())
                output_message.tool_calls = [ToolCall(call_id=call_id, tool_name=tool_name, arguments=tool_params)]

        return 

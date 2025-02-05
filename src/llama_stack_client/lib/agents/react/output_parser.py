# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from ..output_parser import OutputParser
from llama_stack_client.types.shared.completion_message import CompletionMessage
from llama_stack_client.types.shared.tool_call import ToolCall

import json
import uuid

from rich.pretty import pprint


class ReActOutputParser(OutputParser):
    def parse(self, output_message: CompletionMessage) -> CompletionMessage:
        response_text = str(output_message.content)
        try:
            response_json = json.loads(response_text)
            pprint(response_json)
        except json.JSONDecodeError as e:
            print(f"Error parsing action: {e}")
            return output_message

        if response_json.get("answer", None):
            return output_message

        if response_json.get("action", None):
            tool_name = response_json["action"].get("tool_name", None)
            tool_params = response_json["action"].get("tool_params", None)
            if tool_name and tool_params:
                call_id = str(uuid.uuid4())
                output_message.tool_calls = [ToolCall(call_id=call_id, tool_name=tool_name, arguments=tool_params)]

        return output_message

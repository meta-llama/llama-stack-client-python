# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import json
from abc import abstractmethod
from typing import Dict, List, Union

from llama_stack_client.types import ToolResponseMessage, UserMessage
from llama_stack_client.types.tool_def_param import (
    Parameter,
    ToolDefParam,
)


class ClientTool:
    """
    Developers can define their custom tools that models can use
    by extending this class.

    Developers need to provide
        - name
        - description
        - params_definition
        - implement tool's behavior in `run_impl` method

    NOTE: The return of the `run` method needs to be json serializable
    """

    @abstractmethod
    def get_name(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_description(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_params_definition(self) -> Dict[str, Parameter]:
        raise NotImplementedError

    def get_instruction_string(self) -> str:
        return f"Use the function '{self.get_name()}' to: {self.get_description()}"

    def parameters_for_system_prompt(self) -> str:
        return json.dumps(
            {
                "name": self.get_name(),
                "description": self.get_description(),
                "parameters": {
                    name: definition.__dict__
                    for name, definition in self.get_params_definition().items()
                },
            }
        )

    def get_tool_definition(self) -> ToolDefParam:
        return ToolDefParam(
            name=self.get_name(),
            description=self.get_description(),
            parameters=list(self.get_params_definition().values()),
            metadata={},
            tool_prompt_format="python_list",
        )

    @abstractmethod
    def run(
        self, messages: List[Union[UserMessage, ToolResponseMessage]]
    ) -> List[Union[UserMessage, ToolResponseMessage]]:
        raise NotImplementedError

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import json
from abc import abstractmethod
from typing import Callable, Dict, TypeVar, get_type_hints, List, Union, get_origin, get_args
import inspect

from llama_stack_client.types import ToolResponseMessage, UserMessage
from llama_stack_client.types.tool_def_param import Parameter, ToolDefParam


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
                "parameters": {name: definition for name, definition in self.get_params_definition().items()},
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


class SingleMessageClientTool(ClientTool):
    """
    Helper class to handle custom tools that take a single message
    Extending this class and implementing the `run_impl` method will
    allow for the tool be called by the model and the necessary plumbing.
    """

    def run(self, messages: List[Union[UserMessage, ToolResponseMessage]]) -> List[ToolResponseMessage]:
        assert len(messages) == 1, "Expected single message"

        message = messages[0]

        tool_call = message.tool_calls[0]

        try:
            response = self.run_impl(**tool_call.arguments)
            response_str = json.dumps(response, ensure_ascii=False)
        except Exception as e:
            response_str = f"Error when running tool: {e}"

        message = ToolResponseMessage(
            call_id=tool_call.call_id,
            tool_name=tool_call.tool_name,
            content=response_str,
            role="tool",
        )
        return [message]

    @abstractmethod
    def run_impl(self, *args, **kwargs):
        raise NotImplementedError()


T = TypeVar("T", bound=Callable)


def tool(func: T) -> ClientTool:
    """
    Decorator to convert a function into a ClientTool.
    Usage:
        @tool
        def add(x: int, y: int) -> int:
            '''Add 2 integer numbers

            :param x: integer 1
            :param y: integer 2
            :returns: sum of x + y
            '''
            return x + y
    
    Note that you must use RST-style docstrings with :param tags for each parameter. These will be used for prompting model to use tools correctly.  
    :returns: tags in the docstring is optional as it would not be used for the tool's description.
    """


    class WrappedTool(SingleMessageClientTool):
        __name__ = func.__name__
        __doc__ = func.__doc__
        __module__ = func.__module__

        def get_name(self) -> str:
            return func.__name__

        def get_description(self) -> str:
            doc = inspect.getdoc(func)
            if doc:
                # Get everything before the first :param
                return doc.split(":param")[0].strip()
            return ""

        def get_params_definition(self) -> Dict[str, Parameter]:
            hints = get_type_hints(func)
            # Remove return annotation if present
            hints.pop("return", None)

            # Get parameter descriptions from docstring
            params = {}
            sig = inspect.signature(func)
            doc = inspect.getdoc(func) or ""

            for name, type_hint in hints.items():
                # Look for :param name: in docstring
                param_doc = ""
                for line in doc.split("\n"):
                    if line.strip().startswith(f":param {name}:"):
                        param_doc = line.split(":", 2)[2].strip()
                        break
                
                if param_doc == "":
                    raise ValueError(f"No parameter description found for parameter {name}")

                param = sig.parameters[name]
                is_optional_type = get_origin(type_hint) is Union and type(None) in get_args(type_hint)
                is_required = param.default == inspect.Parameter.empty and not is_optional_type
                params[name] = Parameter(
                    name=name,
                    description=param_doc or f"Parameter {name}",
                    parameter_type=type_hint.__name__,
                    default=param.default,
                    required=is_required,
                )
            return params

        def run_impl(self, **kwargs):
            return func(**kwargs)

    return WrappedTool()

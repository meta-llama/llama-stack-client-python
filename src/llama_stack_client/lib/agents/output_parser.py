# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from abc import abstractmethod

from llama_stack_client.types.agents.turn import CompletionMessage


class OutputParser:
    """
    Developers can define their own response output parser to parse the response from the agent turn.

    Developers need to implement the `parse` method to parse the response from the agent turn.
    The return value should be a CompletionMessage object with parsed result popoulated in content and tool_calls.
    """

    @abstractmethod
    def parse(self, output_message: CompletionMessage) -> CompletionMessage:
        raise NotImplementedError

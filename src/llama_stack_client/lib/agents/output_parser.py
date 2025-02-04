# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from abc import abstractmethod

from llama_stack_client.types.agents.turn import CompletionMessage


class OutputParser:
    """
    Abstract base class for parsing agent responses. Implement this class to customize how
    agent outputs are processed and transformed.

    This class allows developers to define custom parsing logic for agent responses,
    which can be useful for:
    - Extracting specific information from the response
    - Formatting or structuring the output in a specific way
    - Validating or sanitizing the agent's response

    To use this class:
    1. Create a subclass of OutputParser
    2. Implement the `parse` method
    3. Pass your parser instance to the Agent's constructor

    Example:
        class MyCustomParser(OutputParser):
            def parse(self, output_message: CompletionMessage) -> CompletionMessage:
                # Add your custom parsing logic here
                return processed_message

    Methods:
        parse(output_message: CompletionMessage) -> CompletionMessage:
            Abstract method that must be implemented by subclasses to process
            the agent's response.

            Args:
                output_message (CompletionMessage): The response message from agent turn

            Returns:
                CompletionMessage: The processed/transformed response message
    """

    @abstractmethod
    def parse(self, output_message: CompletionMessage) -> CompletionMessage:
        raise NotImplementedError

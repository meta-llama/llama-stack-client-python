# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.


# class ReActAgent(Agent):
#     """ReAct agent.

#     Simple wrapper around Agent + ReActOutputParser + ReActPromptTemplate to create a ReAct agent.
#     """
#     def __init__(self, model: str, output_parser: OutputParser, prompt_template: PromptTemplate):
#         super().__init__(model, output_parser, prompt_template)
#         self.output_parser = ReActOutputParser()
#         self.prompt_template = ReActPromptTemplate()

#     @classmethod
#     def create(cls, **kwargs) -> "ReActAgent":
#         return cls(**kwargs)

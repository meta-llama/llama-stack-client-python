# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse

from llama_stack_client.lib.cli.models.get import ModelsGet
from llama_stack_client.lib.cli.models.list import ModelsList
from llama_stack_client.lib.cli.subcommand import Subcommand


class ModelsParser(Subcommand):
    """List details about available models on distribution."""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "models",
            prog="llama-stack-client models",
            description="Query details about available models on Llama Stack distributiom. ",
            formatter_class=argparse.RawTextHelpFormatter,
        )

        subparsers = self.parser.add_subparsers(title="models_subcommands")
        ModelsList.create(subparsers)
        ModelsGet.create(subparsers)

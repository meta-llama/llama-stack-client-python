# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.


import argparse

from llama_stack_client.lib.cli.eval_tasks.list import EvalTasksList

from llama_stack_client.lib.cli.subcommand import Subcommand


class EvalTasksParser(Subcommand):
    """List details about available eval banks type on distribution."""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "eval_tasks",
            prog="llama-stack-client eval_tasks",
            description="Query details about available eval tasks type on distribution.",
            formatter_class=argparse.RawTextHelpFormatter,
        )

        subparsers = self.parser.add_subparsers(title="eval_tasks_subcommands")
        EvalTasksList.create(subparsers)

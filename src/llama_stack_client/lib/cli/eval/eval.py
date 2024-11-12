# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.


import argparse

from llama_stack_client.lib.cli.subcommand import Subcommand

from .run_benchmark import EvalRunBenchmark


class EvalParser(Subcommand):
    """Run evaluation benchmark tasks."""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "eval",
            prog="llama-stack-client eval",
            description="Run evaluation tasks.",
            formatter_class=argparse.RawTextHelpFormatter,
        )

        subparsers = self.parser.add_subparsers(title="eval_subcommands")
        EvalRunBenchmark.create(subparsers)

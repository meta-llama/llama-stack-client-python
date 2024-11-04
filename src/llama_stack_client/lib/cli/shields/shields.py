# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse

from llama_stack_client.lib.cli.shields.list import ShieldsList

from llama_stack_client.lib.cli.subcommand import Subcommand


class ShieldsParser(Subcommand):
    """List details about available safety shields on distribution."""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "shields",
            prog="llama-stack-client shields",
            description="Query details about available safety shields on distribution.",
            formatter_class=argparse.RawTextHelpFormatter,
        )

        subparsers = self.parser.add_subparsers(title="shields_subcommands")
        ShieldsList.create(subparsers)

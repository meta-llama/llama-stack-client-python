# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.


import argparse

from llama_stack_client.lib.cli.memory_banks.list import MemoryBanksList

from llama_stack_client.lib.cli.subcommand import Subcommand


class MemoryBanksParser(Subcommand):
    """List details about available memory banks type on distribution."""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "memory_banks",
            prog="llama-stack-client memory_banks",
            description="Query details about available memory banks type on distribution.",
            formatter_class=argparse.RawTextHelpFormatter,
        )

        subparsers = self.parser.add_subparsers(title="memory_banks_subcommands")
        MemoryBanksList.create(subparsers)

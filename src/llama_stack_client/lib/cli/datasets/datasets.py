# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse

from llama_stack_client.lib.cli.subcommand import Subcommand
from .list import DatasetsList


class DatasetsParser(Subcommand):
    """Parser for datasets commands"""

    @classmethod
    def create(cls, subparsers: argparse._SubParsersAction):
        parser = subparsers.add_parser(
            "datasets",
            help="Manage datasets",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        parser.set_defaults(func=lambda _: parser.print_help())

        # Create subcommands
        datasets_subparsers = parser.add_subparsers(title="subcommands")
        DatasetsList(datasets_subparsers)

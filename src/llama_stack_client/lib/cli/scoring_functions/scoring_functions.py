# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse

from llama_stack_client.lib.cli.subcommand import Subcommand
from .list import ScoringFunctionsList


class ScoringFunctionsParser(Subcommand):
    """Parser for scoring functions commands"""

    @classmethod
    def create(cls, subparsers: argparse._SubParsersAction):
        parser = subparsers.add_parser(
            "scoring_functions",
            help="Manage scoring functions",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        parser.set_defaults(func=lambda _: parser.print_help())

        # Create subcommands
        scoring_functions_subparsers = parser.add_subparsers(title="subcommands")
        ScoringFunctionsList(scoring_functions_subparsers)

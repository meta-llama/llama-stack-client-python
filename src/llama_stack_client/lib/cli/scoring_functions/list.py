# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse

from llama_stack_client import LlamaStackClient
from llama_stack_client.lib.cli.common.utils import print_table_from_response
from llama_stack_client.lib.cli.configure import get_config
from llama_stack_client.lib.cli.subcommand import Subcommand


class ScoringFunctionsList(Subcommand):
    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "list",
            prog="llama-stack-client scoring_functions list",
            description="Show available scoring functions on distribution endpoint",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_scoring_functions_list_cmd)

    def _add_arguments(self):
        self.parser.add_argument(
            "--endpoint",
            type=str,
            help="Llama Stack distribution endpoint",
        )

    def _run_scoring_functions_list_cmd(self, args: argparse.Namespace):
        args.endpoint = get_config().get("endpoint") or args.endpoint

        client = LlamaStackClient(
            base_url=args.endpoint,
        )

        headers = [
            "identifier",
            "provider_id",
            "description",
            "type",
        ]

        scoring_functions_list_response = client.scoring_functions.list()
        if scoring_functions_list_response:
            print_table_from_response(scoring_functions_list_response, headers)

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


class ShieldsList(Subcommand):
    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "list",
            prog="llama-stack-client shields list",
            description="Show available llama models at distribution endpoint",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_shields_list_cmd)

    def _add_arguments(self):
        self.parser.add_argument(
            "--endpoint",
            type=str,
            help="Llama Stack distribution endpoint",
            default="",
        )

    def _run_shields_list_cmd(self, args: argparse.Namespace):
        config = get_config()
        if config:
            args.endpoint = config.get("endpoint")

        if not args.endpoint:
            self.parser.error(
                "A valid endpoint is required. Please run llama-stack-client configure first or pass in a valid endpoint with --endpoint. "
            )
        client = LlamaStackClient(
            base_url=args.endpoint,
        )

        shields_list_response = client.shields.list()

        if shields_list_response:
            print_table_from_response(shields_list_response)

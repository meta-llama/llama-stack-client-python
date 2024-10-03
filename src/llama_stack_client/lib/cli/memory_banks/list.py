# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse
import json

from llama_stack_client import LlamaStackClient
from llama_stack_client.lib.cli.configure import get_config
from llama_stack_client.lib.cli.subcommand import Subcommand

from tabulate import tabulate


class MemoryBanksList(Subcommand):
    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "list",
            prog="llama-stack-client memory_banks list",
            description="Show available memory banks type on distribution endpoint",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_memory_banks_list_cmd)

    def _add_arguments(self):
        self.endpoint = get_config().get("endpoint")
        self.parser.add_argument(
            "--endpoint",
            type=str,
            help="Llama Stack distribution endpoint",
            default=self.endpoint,
        )

    def _run_memory_banks_list_cmd(self, args: argparse.Namespace):
        client = LlamaStackClient(
            base_url=args.endpoint,
        )

        headers = [
            "Memory Bank Type",
            "Provider Type",
            "Provider Config",
        ]

        memory_banks_list_response = client.memory_banks.list()
        rows = []

        for bank_spec in memory_banks_list_response:
            rows.append(
                [
                    bank_spec.bank_type,
                    bank_spec.provider_config.provider_type,
                    json.dumps(bank_spec.provider_config.config, indent=4),
                ]
            )

        print(tabulate(rows, headers=headers, tablefmt="grid"))

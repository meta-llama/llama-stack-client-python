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
        self.parser.add_argument(
            "--endpoint",
            type=str,
            help="Llama Stack distribution endpoint",
        )

    def _run_memory_banks_list_cmd(self, args: argparse.Namespace):
        args.endpoint = get_config().get("endpoint") or args.endpoint

        client = LlamaStackClient(
            base_url=args.endpoint,
        )

        headers = [
            "identifier",
            "provider_id",
            "type",
            "embedding_model",
            "chunk_size_in_tokens",
            "overlap_size_in_tokens",
        ]

        memory_banks_list_response = client.memory_banks.list()
        if memory_banks_list_response:
            print_table_from_response(memory_banks_list_response, headers)

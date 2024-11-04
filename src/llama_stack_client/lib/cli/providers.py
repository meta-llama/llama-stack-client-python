# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse

from tabulate import tabulate

from llama_stack_client import LlamaStackClient
from llama_stack_client.lib.cli.configure import get_config
from llama_stack_client.lib.cli.subcommand import Subcommand


class ProvidersParser(Subcommand):
    """Configure Llama Stack Client CLI"""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "providers",
            prog="llama-stack-client providers",
            description="List available providers Llama Stack Client CLI",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_providers_cmd)

    def _add_arguments(self):
        self.parser.add_argument(
            "--endpoint",
            type=str,
            help="Llama Stack distribution endpoint",
        )

    def _run_providers_cmd(self, args: argparse.Namespace):
        config = get_config()
        if config:
            args.endpoint = config.get("endpoint")

        client = LlamaStackClient(
            base_url=args.endpoint,
        )

        headers = [
            "API",
            "Provider ID",
            "Provider Type",
        ]

        providers_response = client.providers.list()
        rows = []

        for k, v in providers_response.items():
            for provider_info in v:
                rows.append([k, provider_info.provider_id, provider_info.provider_type])

        print(tabulate(rows, headers=headers, tablefmt="grid"))

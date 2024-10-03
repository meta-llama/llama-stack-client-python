# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import json
import argparse

from tabulate import tabulate

from llama_stack_client import LlamaStackClient
from llama_stack_client.lib.cli.configure import get_config
from llama_stack_client.lib.cli.subcommand import Subcommand


class ModelsList(Subcommand):
    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "list",
            prog="llama-stack-client models list",
            description="Show available llama models at distribution endpoint",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_models_list_cmd)

    def _add_arguments(self):
        self.endpoint = get_config().get("endpoint")
        self.parser.add_argument(
            "--endpoint",
            type=str,
            help="Llama Stack distribution endpoint",
            default=self.endpoint,
        )

    def _run_models_list_cmd(self, args: argparse.Namespace):
        client = LlamaStackClient(
            base_url=args.endpoint,
        )

        headers = [
            "Model ID (model)",
            "Model Metadata",
            "Provider Type",
            "Provider Config",
        ]

        models_list_response = client.models.list()
        rows = []

        for model_spec in models_list_response:
            rows.append(
                [
                    model_spec.llama_model["core_model_id"],
                    json.dumps(model_spec.llama_model, indent=4),
                    model_spec.provider_config.provider_type,
                    json.dumps(model_spec.provider_config.config, indent=4),
                ]
            )

        print(tabulate(rows, headers=headers, tablefmt="grid"))

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


class ModelsGet(Subcommand):
    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "get",
            prog="llama-stack-client models get",
            description="Show available llama models at distribution endpoint",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_models_list_cmd)

    def _add_arguments(self):
        self.parser.add_argument(
            "model_id",
            type=str,
            help="Model ID to query information about",
        )

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

        models_get_response = client.models.get(core_model_id=args.model_id)

        if not models_get_response:
            print(
                f"Model {args.model_id} is not found at distribution endpoint {args.endpoint}. Please ensure endpoint is serving specified model. "
            )
            return

        rows = []
        rows.append(
            [
                models_get_response.llama_model["core_model_id"],
                json.dumps(models_get_response.llama_model, indent=4),
                models_get_response.provider_config.provider_type,
                json.dumps(models_get_response.provider_config.config, indent=4),
            ]
        )

        print(tabulate(rows, headers=headers, tablefmt="grid"))

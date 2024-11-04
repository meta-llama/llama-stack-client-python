# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse
import os

import yaml

from llama_stack_client.lib.cli.constants import get_config_file_path
from llama_stack_client.lib.cli.subcommand import Subcommand


def get_config():
    config_file = get_config_file_path()
    if config_file.exists():
        with open(config_file, "r") as f:
            return yaml.safe_load(f)
    return None


class ConfigureParser(Subcommand):
    """Configure Llama Stack Client CLI"""

    def __init__(self, subparsers: argparse._SubParsersAction):
        super().__init__()
        self.parser = subparsers.add_parser(
            "configure",
            prog="llama-stack-client configure",
            description="Configure Llama Stack Client CLI",
            formatter_class=argparse.RawTextHelpFormatter,
        )
        self._add_arguments()
        self.parser.set_defaults(func=self._run_configure_cmd)

    def _add_arguments(self):
        self.parser.add_argument(
            "--host",
            type=str,
            help="Llama Stack distribution host",
        )
        self.parser.add_argument(
            "--port",
            type=str,
            help="Llama Stack distribution port number",
        )
        self.parser.add_argument(
            "--endpoint",
            type=str,
            help="Llama Stack distribution endpoint",
        )

    def _run_configure_cmd(self, args: argparse.Namespace):
        from prompt_toolkit import prompt
        from prompt_toolkit.validation import Validator

        os.makedirs(LLAMA_STACK_CLIENT_CONFIG_DIR, exist_ok=True)
        config_path = get_config_file_path()

        if args.endpoint:
            endpoint = args.endpoint
        else:
            if args.host and args.port:
                endpoint = f"http://{args.host}:{args.port}"
            else:
                host = prompt(
                    "> Enter the host name of the Llama Stack distribution server: ",
                    validator=Validator.from_callable(
                        lambda x: len(x) > 0,
                        error_message="Host cannot be empty, please enter a valid host",
                    ),
                )
                port = prompt(
                    "> Enter the port number of the Llama Stack distribution server: ",
                    validator=Validator.from_callable(
                        lambda x: x.isdigit(),
                        error_message="Please enter a valid port number",
                    ),
                )
                endpoint = f"http://{host}:{port}"

        with open(config_path, "w") as f:
            f.write(
                yaml.dump(
                    {
                        "endpoint": endpoint,
                    },
                    sort_keys=True,
                )
            )

        print(f"Done! You can now use the Llama Stack Client CLI with endpoint {endpoint}")

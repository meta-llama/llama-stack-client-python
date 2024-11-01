# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse

from llama_stack_client.lib.cli.constants import get_config_file_path

from .configure import ConfigureParser
from .memory_banks import MemoryBanksParser

from .models import ModelsParser
from .providers import ProvidersParser
from .shields import ShieldsParser


class LlamaStackClientCLIParser:
    """Define CLI parse for LlamaStackClient CLI"""

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="llama-stack-client",
            description="Welcome to the LlamaStackClient CLI",
        )
        # Default command is to print help
        self.parser.set_defaults(func=lambda _: self.parser.print_help())

        subparsers = self.parser.add_subparsers(title="subcommands")

        # add sub-commands
        ModelsParser.create(subparsers)
        MemoryBanksParser.create(subparsers)
        ShieldsParser.create(subparsers)
        ConfigureParser.create(subparsers)
        ProvidersParser.create(subparsers)

    def parse_args(self) -> argparse.Namespace:
        return self.parser.parse_args()

    def run(self, args: argparse.Namespace) -> None:
        if not get_config_file_path().exists():
            print(
                "Config file not found. Please run 'llama-stack-client configure' to create one."
            )
            return

        args.func(args)


def main():
    parser = LlamaStackClientCLIParser()
    args = parser.parse_args()
    parser.run(args)


if __name__ == "__main__":
    main()

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import argparse

from .configure import ConfigureParser
from .providers import ProvidersParser
from .memory_banks import MemoryBanksParser

from .models import ModelsParser
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
        args.func(args)


def main():
    parser = LlamaStackClientCLIParser()
    args = parser.parse_args()
    parser.run(args)


if __name__ == "__main__":
    main()

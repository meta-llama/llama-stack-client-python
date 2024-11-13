# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click

from .list import list_memory_banks


@click.group()
def memory_banks():
    """Query details about available memory banks type on distribution."""
    pass


# Register subcommands
memory_banks.add_command(list_memory_banks)

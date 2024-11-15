# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.
import click

from .list import list_datasets
from .register import register


@click.group()
def datasets():
    """Query details about available datasets on Llama Stack distribution."""
    pass


# Register subcommands
datasets.add_command(list_datasets)
datasets.add_command(register)

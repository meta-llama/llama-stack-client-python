# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click
from llama_stack_client.lib.cli.models.get import get_model
from llama_stack_client.lib.cli.models.list import list_models


@click.group()
def models():
    """Query details about available models on Llama Stack distribution."""
    pass


# Register subcommands
models.add_command(list_models)
models.add_command(get_model)

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click

from llama_stack_client.lib.cli.common.utils import print_table_from_response


@click.command("list")
@click.pass_context
def list_memory_banks(ctx):
    """Show available memory banks on distribution endpoint"""

    client = ctx.obj["client"]

    headers = [
        "identifier",
        "provider_id",
        "description",
        "type",
    ]

    memory_banks_list_response = client.memory_banks.list()
    if memory_banks_list_response:
        print_table_from_response(memory_banks_list_response, headers)

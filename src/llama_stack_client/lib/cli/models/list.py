# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click

from llama_stack_client.lib.cli.common.utils import print_table_from_response


@click.command(name="list", help="Show available llama models at distribution endpoint")
@click.pass_context
def list_models(ctx):
    client = ctx.obj["client"]

    headers = ["identifier", "provider_id", "provider_resource_id", "metadata"]
    response = client.models.list()
    if response:
        print_table_from_response(response, headers)

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click

from llama_stack_client.lib.cli.common.utils import print_table_from_response


@click.command("list")
@click.pass_context
def list_scoring_functions(ctx):
    """Show available scoring functions on distribution endpoint"""

    client = ctx.obj["client"]

    headers = [
        "identifier",
        "provider_id",
        "description",
        "type",
    ]

    scoring_functions_list_response = client.scoring_functions.list()
    if scoring_functions_list_response:
        print_table_from_response(scoring_functions_list_response, headers)

# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import click
from tabulate import tabulate


@click.command(name="get")
@click.argument("model_id")
@click.pass_context
def get_model(ctx, model_id: str):
    """Show available llama models at distribution endpoint"""
    client = ctx.obj["client"]

    models_get_response = client.models.retrieve(identifier=model_id)

    if not models_get_response:
        click.echo(
            f"Model {model_id} is not found at distribution endpoint. "
            "Please ensure endpoint is serving specified model."
        )
        return

    headers = sorted(models_get_response.__dict__.keys())
    rows = []
    rows.append([models_get_response.__dict__[headers[i]] for i in range(len(headers))])

    click.echo(tabulate(rows, headers=headers, tablefmt="grid"))

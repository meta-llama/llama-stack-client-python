# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from typing import Optional

import click
import yaml
from rich.console import Console
from rich.table import Table

from ..common.utils import handle_client_errors


@click.group()
def shields():
    """Query details about available safety shields on distribution."""
    pass


@click.command("list")
@click.pass_context
@handle_client_errors("list shields")
def list(ctx):
    """Show available safety shields on distribution endpoint"""
    client = ctx.obj["client"]
    console = Console()

    shields_list_response = client.shields.list()
    headers = []
    if shields_list_response and len(shields_list_response) > 0:
        headers = sorted(shields_list_response[0].__dict__.keys())

    if shields_list_response:
        table = Table()
        for header in headers:
            table.add_column(header)

        for item in shields_list_response:
            table.add_row(*[str(getattr(item, header)) for header in headers])
        console.print(table)


@shields.command()
@click.option("--shield-id", required=True, help="Id of the shield")
@click.option("--provider-id", help="Provider ID for the shield", default=None)
@click.option("--provider-shield-id", help="Provider's shield ID", default=None)
@click.option("--params", type=str, help="JSON configuration parameters for the shield", default=None)
@click.pass_context
@handle_client_errors("register shield")
def register(
    ctx,
    shield_id: str,
    provider_id: Optional[str],
    provider_shield_id: Optional[str],
    params: Optional[str],
):
    """Register a new safety shield"""
    client = ctx.obj["client"]

    response = client.shields.register(
        shield_id=shield_id,
        params=params,
        provider_id=provider_id,
        provider_shield_id=provider_shield_id,
    )
    if response:
        click.echo(yaml.dump(response.dict()))


# Register subcommands
shields.add_command(list)
shields.add_command(register)

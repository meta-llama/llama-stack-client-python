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
def memory_banks():
    """Query details about available memory banks type on distribution."""
    pass


@click.command("list")
@click.pass_context
@handle_client_errors("list memory banks")
def list(ctx):
    """Show available memory banks on distribution endpoint"""

    client = ctx.obj["client"]
    console = Console()
    memory_banks_list_response = client.memory_banks.list()

    if memory_banks_list_response:
        table = Table()
        # Add our specific columns
        table.add_column("identifier")
        table.add_column("provider_id")
        table.add_column("provider_resource_id")
        table.add_column("memory_bank_type")
        table.add_column("params")

        for item in memory_banks_list_response:
            # Create a dict of all attributes
            item_dict = item.__dict__

            # Extract our main columns
            identifier = str(item_dict.pop("identifier", ""))
            provider_id = str(item_dict.pop("provider_id", ""))
            provider_resource_id = str(item_dict.pop("provider_resource_id", ""))
            memory_bank_type = str(item_dict.pop("memory_bank_type", ""))
            # Convert remaining attributes to YAML string for params column
            params = yaml.dump(item_dict, default_flow_style=False)

            table.add_row(identifier, provider_id, provider_resource_id, memory_bank_type, params)

        console.print(table)


@memory_banks.command()
@click.argument("memory-bank-id")
@click.option("--type", type=click.Choice(["vector", "keyvalue", "keyword", "graph"]), required=True)
@click.option("--provider-id", help="Provider ID for the memory bank", default=None)
@click.option("--provider-memory-bank-id", help="Provider's memory bank ID", default=None)
@click.option(
    "--chunk-size",
    type=int,
    help="Chunk size in tokens (for vector type)",
    default=512,
)
@click.option(
    "--embedding-model",
    type=str,
    help="Embedding model (for vector type)",
    default="all-MiniLM-L6-v2",
)
@click.option(
    "--overlap-size",
    type=int,
    help="Overlap size in tokens (for vector type)",
    default=64,
)
@click.pass_context
@handle_client_errors("register memory bank")
def register(
    ctx,
    memory_bank_id: str,
    type: str,
    provider_id: Optional[str],
    provider_memory_bank_id: Optional[str],
    chunk_size: Optional[int],
    embedding_model: Optional[str],
    overlap_size: Optional[int],
):
    """Create a new memory bank"""
    client = ctx.obj["client"]

    config = None
    if type == "vector":
        config = {
            "memory_bank_type": "vector",
            "chunk_size_in_tokens": chunk_size,
            "embedding_model": embedding_model,
        }
        if overlap_size:
            config["overlap_size_in_tokens"] = overlap_size
    elif type == "keyvalue":
        config = {"memory_bank_type": "keyvalue"}
    elif type == "keyword":
        config = {"memory_bank_type": "keyword"}
    elif type == "graph":
        config = {"memory_bank_type": "graph"}

    from rich import print as rprint
    from rich.pretty import pprint

    rprint("\n[bold blue]Memory Bank Configuration:[/bold blue]")
    pprint(config, expand_all=True)

    response = client.memory_banks.register(
        memory_bank_id=memory_bank_id,
        params=config,
        provider_id=provider_id,
        provider_memory_bank_id=provider_memory_bank_id,
    )
    if response:
        click.echo(yaml.dump(response.dict()))


@memory_banks.command()
@click.argument("memory-bank-id")
@click.pass_context
@handle_client_errors("delete memory bank")
def unregister(ctx, memory_bank_id: str):
    """Delete a memory bank"""
    client = ctx.obj["client"]
    client.memory_banks.unregister(memory_bank_id=memory_bank_id)
    click.echo(f"Memory bank '{memory_bank_id}' deleted successfully")


# Register subcommands
memory_banks.add_command(list)
memory_banks.add_command(register)
memory_banks.add_command(unregister)
